import json
import random
import re
import threading
import uuid
import urllib.request
import urllib.parse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q, Avg, Max, Count
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils import timezone
from .models import (
    Course, Category, TypingScore, UserVideoUnlock, HomeworkSubmission, UserProfile,
    Notification, LessonNote, LessonQuestion, Announcement, Certificate, DirectionChangeRequest
)
from .telegram_bot import (
    TELEGRAM_BOT_TOKEN, TELEGRAM_BOT_USERNAME, TEACHER_CHAT_ID,
    send_telegram_raw_message, notify_teacher_new_request,
    notify_student_approved, notify_student_rejected
)


# ============================================================================
# TELEGRAM BOT XABARNOMASI
# ============================================================================
TELEGRAM_BOT_TOKEN = '8957411415:AAEhNbw_-mGuyiLG1zxCbd7cavng9AOiqhE'
TELEGRAM_CHAT_ID = '8623359226'


def send_telegram_bot_message(message_text):
    """
    Ixtiyoriy formatlangan xabarni Telegram bot orqali guruh/kanal/chatga asinxron yuboradi.
    """
    def _send():
        try:
            data = urllib.parse.urlencode({
                'chat_id': TELEGRAM_CHAT_ID,
                'text': message_text,
                'parse_mode': 'HTML'
            }).encode('utf-8')

            url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
            req = urllib.request.Request(url, data=data, method='POST')
            req.add_header('Content-Type', 'application/x-www-form-urlencoded')
            urllib.request.urlopen(req, timeout=10)
        except Exception as e:
            print(f'[Telegram xabar yuborishda xatolik]: {e}')

    thread = threading.Thread(target=_send, daemon=True)
    thread.start()


def send_telegram_notification(full_name, email, username):
    """
    Yangi foydalanuvchi ro'yxatdan o'tganda Telegram botga xabar yuboradi.
    """
    now = timezone.now().strftime('%d.%m.%Y %H:%M:%S')
    total_users = User.objects.count()

    message = (
        f"🆕 <b>Yangi foydalanuvchi ro'yxatdan o'tdi!</b>\n\n"
        f"👤 <b>Ism:</b> {full_name}\n"
        f"📧 <b>Email:</b> {email}\n"
        f"🔑 <b>Username:</b> {username}\n"
        f"🕐 <b>Vaqt:</b> {now}\n\n"
        f"📊 <b>Jami foydalanuvchilar:</b> {total_users} ta\n\n"
        f"🎓 <i>Learnify Online Ta'lim Platformasi</i>"
    )
    send_telegram_bot_message(message)



def portal_view(request):
    """
    Katta Bosh Birlashgan Portal (Gateway):
    Localhost ochilganda to'g'ridan-to'g'ri 2 ta platforma tanlovi chiqadi:
    1. 🎓 Teacher & Ustoz Platformasi (Login: rixsi, Parol: 123456)
    2. 🧑‍🎓 Learnify Talabalar Platformasi
    """
    total_students = User.objects.filter(is_superuser=False).count()
    total_courses = Course.objects.count()
    total_homeworks = HomeworkSubmission.objects.count()
    return render(request, 'portal.html', {
        'total_students': total_students,
        'total_courses': total_courses,
        'total_homeworks': total_homeworks,
    })


def home_view(request):
    """
    Learnify asosiy o'quv platformasi bosh sahifasi:
    - O'quvchi o'z yo'nalishi (masalan: Web Dasturlash) bo'yicha kirganda, boshqa kurslar
      ko'rinmaydi (until u web dasturlashni tugatmaguncha).
    - Tugatganidan keyin ekranda Tabriknoma va yangi o'qilmagan kurslar ro'yxati chiqadi.
    """
    if not request.user.is_authenticated:
        return redirect('register')

    if not request.user.is_superuser:
        u_prof = getattr(request.user, 'profile', None)
        if u_prof and u_prof.role == 'student' and (not u_prof.is_approved or u_prof.approval_status != 'approved'):
            from django.contrib.auth import logout
            logout(request)
            messages.warning(request, "Ustoz taklifnomangizni qabul qilmaguncha tizimga kira olmaysiz.")
            return redirect('login')

    profile, _ = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={'role': 'student', 'group_name': 'FN-24', 'direction': 'Web Dasturlash'}
    )

    direction_slug = profile.get_direction_slug()
    completed_slugs = profile.get_completed_directions_list()
    is_direction_completed = profile.is_current_direction_completed()

    all_categories = Category.objects.all()
    all_courses = Course.objects.all()

    # Kurslar ko'rinish filtri:
    # 1. Agar kurs hali tugatilmagan bo'lsa -> faqat o'z yo'nalishi kurslari ko'rinadi
    # 2. Agar kurs tugatilgan bo'lsa -> Tabriknoma va yangi o'qilmagan kurslar ro'yxati chiqadi
    if not is_direction_completed:
        categories = all_categories.filter(slug=direction_slug)
        courses = all_courses.filter(category__slug=direction_slug)
        unstudied_courses = Course.objects.none()
        completed_courses = Course.objects.none()
        show_congratulations = False
    else:
        show_congratulations = True
        categories = all_categories
        completed_courses = all_courses.filter(category__slug__in=completed_slugs)
        unstudied_courses = all_courses.exclude(category__slug__in=completed_slugs)
        courses = unstudied_courses

    # Qidiruv va kategoriya filtri
    q = request.GET.get('q', '').strip()
    category_slug = request.GET.get('category', '').strip()

    if q:
        courses = courses.filter(
            Q(title__icontains=q) |
            Q(short_description__icontains=q) |
            Q(instructor_name__icontains=q)
        )

    selected_category = None
    if category_slug:
        if is_direction_completed or category_slug == direction_slug:
            selected_category = get_object_or_404(Category, slug=category_slug)
            courses = courses.filter(category=selected_category)

    featured_courses = courses[:6]
    total_students = sum(c.students_count for c in courses)

    user_certificate = None
    if request.user.is_authenticated:
        user_certificate = Certificate.objects.filter(user=request.user, direction_slug=direction_slug).first()

    # Kutilayotgan yangi yo'nalish so'rovi (priglasheniya)
    pending_direction_request = None
    if request.user.is_authenticated:
        pending_direction_request = DirectionChangeRequest.objects.filter(user=request.user, status='pending').first()

    # Barcha o'rganish mumkin bo'lgan yo'nalishlar katalogi
    all_direction_options = [
        {'slug': 'python-backend', 'name': 'Python Backend', 'icon': 'fa-brands fa-python', 'desc': 'Django, PostgreSQL, REST API, Server arxitekturasi'},
        {'slug': 'web-dasturlash', 'name': 'Web Dasturlash', 'icon': 'fa-solid fa-code', 'desc': 'HTML5, CSS3, JavaScript, React.js zamonaviy veb ilovalar'},
        {'slug': 'ai-data-science', 'name': "Sun'iy Intellekt & Data Science", 'icon': 'fa-solid fa-brain', 'desc': 'Machine Learning, Deep Learning, Neyron tarmoqlar, Pandas'},
        {'slug': 'mobile-dev', 'name': 'Mobil Dasturlash (Flutter)', 'icon': 'fa-solid fa-mobile-screen', 'desc': 'Flutter, Dart, iOS va Android mobil ilovalar'},
        {'slug': 'ui-ux-design', 'name': 'UI/UX Dizayn', 'icon': 'fa-solid fa-palette', 'desc': 'Figma, Prototyping, Wireframing, Dizayn tizimlari'},
        {'slug': 'kiberxavfsizlik', 'name': 'Kiberxavfsizlik', 'icon': 'fa-solid fa-shield-halved', 'desc': 'Axborot xavfsizligi, Tarmoq himoyasi, Etik xakerlik'},
    ]
    # Hali o'rganilmagan yo'nalishlar
    available_next_directions = [d for d in all_direction_options if d['slug'] not in completed_slugs]

    context = {
        'categories': categories,
        'courses': courses,
        'unstudied_courses': unstudied_courses,
        'completed_courses': completed_courses,
        'featured_courses': featured_courses,
        'selected_category': selected_category,
        'search_query': q,
        'user_direction': profile.direction,
        'user_direction_slug': direction_slug,
        'is_direction_completed': is_direction_completed,
        'show_congratulations': show_congratulations,
        'completed_slugs': completed_slugs,
        'total_courses_count': courses.count(),
        'total_students_count': total_students or 15000,
        'user_certificate': user_certificate,
        'pending_direction_request': pending_direction_request,
        'available_next_directions': available_next_directions,
    }
    return render(request, 'courses/home.html', context)


def complete_direction_view(request):
    """
    O'quvchi joriy kursni muvaffaqiyatli tugatganda (yoki tugatish tugmasini bosganda):
    - Yo'nalishni tugatilgan deb saqlaydi
    - Rasmiy QR-kodli Sertifikat generatsiya qiladi
    - Bildirishnoma (Notification) va Telegram bot xabarini yuboradi
    - Tabriknoma ma'lumotlari va yangi o'qilmagan kurslar ro'yxatini qaytaradi
    """
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'error': 'Avval tizimga kiring'}, status=401)

    profile, _ = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={'role': 'student', 'group_name': 'FN-24', 'direction': 'Web Dasturlash'}
    )

    old_direction = profile.direction
    slug = profile.get_direction_slug()

    if not (profile.final_test_score and profile.final_test_score >= 75):
        return JsonResponse({
            'success': False,
            'error': "Kursni o'zingizcha yakunlay olmaysiz! Avval barcha darslarni tugatib, ustoz bergan 30 talik yakuniy testdan kamida 75% to'plashingiz shart."
        }, status=403)

    profile.complete_current_direction()

    # Sertifikat yaratish yoki mavjudini olish
    student_full_name = request.user.get_full_name() or request.user.first_name or request.user.username
    cert_id = f"LRN-{timezone.now().strftime('%Y%m')}-{uuid.uuid4().hex[:6].upper()}"
    
    cert, created = Certificate.objects.get_or_create(
        user=request.user,
        direction_slug=slug,
        defaults={
            'certificate_id': cert_id,
            'full_name': student_full_name,
            'direction': old_direction,
            'avg_score': 9.8,
        }
    )

    # Bildirishnoma yuborish
    Notification.objects.create(
        user=request.user,
        title="Tabriklaymiz! Sertifikatingiz tayyor 🎓",
        message=f"Siz '{old_direction}' kursini a'lo baholarga tamomladingiz. QR-kodli rasmiy sertifikatingizni yuklab oling!",
        link=f"/certificate/{cert.certificate_id}/",
        icon="award"
    )

    # Telegram bot orqali tabrik xabari
    send_telegram_bot_message(
        f"🎓 <b>Kurs Muvaffaqiyatli Tamomlandi!</b>\n\n"
        f"👤 <b>Talaba:</b> {cert.full_name}\n"
        f"🏆 <b>Tugatilgan kurs:</b> {cert.direction}\n"
        f"🏅 <b>Sertifikat ID:</b> <code>{cert.certificate_id}</code>\n"
        f"⭐️ <b>Yakuniy o'rtacha ball:</b> {cert.avg_score}/10 ball\n\n"
        f"🌐 <i>Learnify Online Ta'lim Platformasi</i>"
    )

    completed_slugs = profile.get_completed_directions_list()
    unstudied = Course.objects.exclude(category__slug__in=completed_slugs)

    unstudied_list = []
    for c in unstudied:
        unstudied_list.append({
            'title': c.title,
            'slug': c.slug,
            'category_name': c.category.name,
            'category_slug': c.category.slug,
            'duration_hours': c.duration_hours,
            'lessons_count': c.lessons_count,
            'instructor': c.instructor_name,
        })

    return JsonResponse({
        'success': True,
        'message': f"Tabriklaymiz, {student_full_name}! Siz '{old_direction}' kursini muvaffaqiyatli tamomladingiz! 🎓🎉",
        'completed_direction': old_direction,
        'unstudied_courses': unstudied_list,
        'certificate_id': cert.certificate_id,
        'certificate_url': f"/certificate/{cert.certificate_id}/",
    })



def enroll_next_direction_view(request):
    """
    Kursni tamomlagan o'quvchi yangi o'qilmagan kursga yozilishi (yo'nalishini o'zgartirish)
    """
    if not request.user.is_authenticated:
        return redirect('register')

    new_cat_slug = request.POST.get('category_slug') or request.GET.get('category_slug')
    if new_cat_slug:
        cat = get_object_or_404(Category, slug=new_cat_slug)
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        profile.direction = cat.name
        profile.save(update_fields=['direction'])
        messages.success(request, f"Yangi '{cat.name}' kursiga muvaffaqiyatli a'zo bo'ldingiz! O'rganishni boshlang! 🚀")

    return redirect('videos')


def course_detail_view(request, slug):
    """Kurs haqida batafsil sahifa"""
    if not request.user.is_authenticated:
        return redirect('register')
    course = get_object_or_404(Course, slug=slug)
    related_courses = Course.objects.filter(category=course.category).exclude(id=course.id)[:3]
    return render(request, 'courses/detail.html', {
        'course': course,
        'related_courses': related_courses
    })


def coding_view(request):
    """Vibe Coding olib tashlandi, to'g'ridan-to'g'ri video darslarga yo'naltiriladi"""
    return redirect('videos')


def web_dev_view(request):
    """
    Web Dasturlash bo'limi:
    Frontend (HTML, CSS, JS, React) va Backend (Python, Django, PostgreSQL)
    o'quv xaritasi (Roadmap) va topshiriqlar.
    """
    if not request.user.is_authenticated:
        return redirect('register')
    modules = [
        {
            "id": 1,
            "title": "Frontend Asoslari: HTML5, CSS3 & Responsive Design",
            "desc": "Zamonaviy veb-sahifalar yaratish, Flexbox, CSS Grid, animatsiyalar va mobil moslashuvchanlik.",
            "duration": "18 soat",
            "lessons_count": 24,
            "status": "Kutilmoqda",
            "progress": 0,
            "color": "#38bdf8"
        },
        {
            "id": 2,
            "title": "JavaScript (ES6+) & DOM bilan interaktivlik",
            "desc": "O'zgaruvchilar, massivlar, obyektlar, async/await, Fetch API va brauzer hodisalari bilan ishlash.",
            "duration": "26 soat",
            "lessons_count": 32,
            "status": "Kutilmoqda",
            "progress": 0,
            "color": "#f59e0b"
        },
        {
            "id": 3,
            "title": "React.js: Zamonaviy SPA va State Management",
            "desc": "Komponentlar, Hooks (useState, useEffect, useMemo), Redux Toolkit va TailwindCSS integratsiyasi.",
            "duration": "30 soat",
            "lessons_count": 38,
            "status": "Kutilmoqda",
            "progress": 0,
            "color": "#06b6d4"
        },
        {
            "id": 4,
            "title": "Python & Django Backend: REST API va Ma'lumotlar Bazasi",
            "desc": "ORM, PostgreSQL, autentifikatsiya, JWT tokenlar, xavfsizlik va Docker konteynerlashtirish.",
            "duration": "40 soat",
            "lessons_count": 46,
            "status": "Kutilmoqda",
            "progress": 0,
            "color": "#a855f7"
        },
    ]

    context = {
        'modules': modules,
    }
    return render(request, 'dashboard/web_dev.html', context)


def videos_view(request):
    """Video Darslar bo'limi — Har bir yo'nalish uchun real YouTube videolar"""
    if not request.user.is_authenticated:
        return redirect('register')
    if not request.user.is_superuser:
        u_prof = getattr(request.user, 'profile', None)
        if u_prof and u_prof.role == 'student' and (not u_prof.is_approved or u_prof.approval_status != 'approved'):
            from django.contrib.auth import logout
            logout(request)
            messages.warning(request, "Ustoz taklifnomangizni qabul qilmaguncha tizimga kira olmaysiz.")
            return redirect('login')
    courses = Course.objects.all()
    categories = Category.objects.all()

    # Tanlangan kategoriya
    selected_slug = request.GET.get('category', '').strip()

    # Har bir yo'nalish uchun 10 tadan mukammal va ketma-ketlikdagi video darslar
    import copy
    from Courses.curriculum_data import CURRICULUM_DATA
    video_library = copy.deepcopy(CURRICULUM_DATA)

    # O'quvchining yo'nalishi va kursni tugatganlik holati:
    profile, _ = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={'role': 'student', 'group_name': 'FN-24', 'direction': 'Web Dasturlash'}
    )
    direction_slug = profile.get_direction_slug()
    is_direction_completed = profile.is_current_direction_completed()
    completed_slugs = profile.get_completed_directions_list()

    # O'quvchi faqat o'z yo'nalishidagi videolarni ko'rishi shart:
    # Masalan: Yo'nalish Cybersecurity bo'lsa, faqat Kiberxavfsizlik videolari ko'rinadi!
    if not request.user.is_superuser and getattr(profile, 'role', 'student') == 'student':
        selected_slug = direction_slug
        if direction_slug in video_library:
            video_library = {direction_slug: video_library[direction_slug]}
    elif not is_direction_completed and request.user.username != 'rixsi' and not request.user.is_superuser:
        selected_slug = direction_slug

    # Tanlangan kategoriya
    if selected_slug and selected_slug in video_library:
        current_section = video_library[selected_slug]
    else:
        selected_slug = direction_slug if direction_slug in video_library else 'web-dasturlash'
        current_section = video_library[selected_slug]

    # Boshqa yo'nalishlar umuman ko'rinmasin — faqat joriy bitta yo'nalish
    video_library = {selected_slug: current_section}

    # Tanlangan video
    selected_video_id = request.GET.get('video', '1')
    try:
        selected_video_id = int(selected_video_id)
    except ValueError:
        selected_video_id = 1

    current_video = None
    for v in current_section['videos']:
        if v['id'] == selected_video_id:
            current_video = v
            break
    if not current_video:
        current_video = current_section['videos'][0]

    # Superadmin huquqlari va ruxsat berilgan qulfdan chiqarishlar
    is_superadmin = request.user.is_authenticated and request.user.is_superuser
    
    # Hamma uchun yoki joriy user uchun qulfdan chiqarilganmi?
    unlocked_for_all = UserVideoUnlock.objects.filter(unlocked_for_all_users=True, category_slug__in=['all', selected_slug]).exists()

    # Har bir darsning qulf holatini aniqlash (Ustoz ochgan darslargina ochiladi!)
    unlocked_ids = set()
    if is_superadmin or unlocked_for_all:
        unlocked_ids = {v['id'] for v in current_section['videos']}
    elif request.user.is_authenticated:
        # 1-dars har doim boshlang'ich tanishtiruv sifatida ochiq bo'ladi
        unlocked_ids.add(1)
        # Ustoz ochib bergan aniq darslar
        user_unlocks = UserVideoUnlock.objects.filter(
            Q(user=request.user) & 
            (Q(category_slug='all') | Q(category_slug=selected_slug))
        )
        for u in user_unlocks:
            if u.lesson_id == 0:
                unlocked_ids.update({v['id'] for v in current_section['videos']})
            else:
                unlocked_ids.add(u.lesson_id)

    for v in current_section['videos']:
        v['is_unlocked'] = (v['id'] in unlocked_ids)

    # Tanlangan video ochiqmi?
    current_video_is_unlocked = (selected_video_id in unlocked_ids)

    # O'quvchining ushbu yo'nalish bo'yicha topshirgan vazifalari va qo'yilgan baholari
    user_homeworks = []
    if request.user.is_authenticated:
        user_homeworks = HomeworkSubmission.objects.filter(
            user=request.user,
            category_slug=selected_slug
        ).order_by('-submitted_at')

    # Superadmin / Teacher uchun oddiy foydalanuvchilar ro'yxati
    all_users = []
    if is_superadmin or request.user.is_staff:
        all_users = User.objects.filter(is_superuser=False).order_by('username')

    # Dars Konspekti (Shaxsiy eslatma)
    current_note = ""
    if request.user.is_authenticated:
        note_obj = LessonNote.objects.filter(
            user=request.user,
            category_slug=selected_slug,
            lesson_id=selected_video_id
        ).first()
        if note_obj:
            current_note = note_obj.content

    # Dars bo'yicha Ustozga berilgan savollar (Q&A)
    lesson_questions = LessonQuestion.objects.filter(
        category_slug=selected_slug,
        lesson_id=selected_video_id
    ).select_related('user', 'answered_by').order_by('-created_at')

    # Foydalanuvchining sertifikati (agar kurs tugatilgan bo'lsa)
    user_certificate = None
    if request.user.is_authenticated:
        user_certificate = Certificate.objects.filter(user=request.user, direction_slug=direction_slug).first()

    # Kutilayotgan yangi yo'nalish so'rovi (priglasheniya)
    pending_direction_request = None
    if request.user.is_authenticated:
        pending_direction_request = DirectionChangeRequest.objects.filter(user=request.user, status='pending').first()

    # Barcha o'rganish mumkin bo'lgan yo'nalishlar katalogi
    all_direction_options = [
        {'slug': 'python-backend', 'name': 'Python Backend', 'icon': 'fa-brands fa-python', 'color': '#a855f7', 'desc': "Django, PostgreSQL, REST API, Server arxitekturasi va ma'lumotlar bazasi"},
        {'slug': 'web-dasturlash', 'name': 'Web Dasturlash', 'icon': 'fa-solid fa-code', 'color': '#38bdf8', 'desc': "HTML5, CSS3, JavaScript, React.js zamonaviy Frontend va Fullstack"},
        {'slug': 'ai-data-science', 'name': "Sun'iy Intellekt & Data Science", 'icon': 'fa-solid fa-brain', 'color': '#ec4899', 'desc': "Machine Learning, Deep Learning, Neyron tarmoqlar va Big Data"},
        {'slug': 'mobile-dev', 'name': 'Mobil Dasturlash (Flutter)', 'icon': 'fa-solid fa-mobile-screen', 'color': '#10b981', 'desc': "Flutter, Dart, iOS va Android mobil ilovalar yaratish"},
        {'slug': 'ui-ux-design', 'name': 'UI/UX Dizayn', 'icon': 'fa-solid fa-palette', 'color': '#f59e0b', 'desc': "Figma, Prototyping, Wireframing va zamonaviy interfeys dizaynlari"},
        {'slug': 'kiberxavfsizlik', 'name': 'Kiberxavfsizlik', 'icon': 'fa-solid fa-shield-halved', 'color': '#ef4444', 'desc': "Axborot xavfsizligi, Tarmoq himoyasi, Etik xakerlik va Pentesting"},
    ]
    # Hali o'rganilmagan yo'nalishlar
    available_next_directions = [d for d in all_direction_options if d['slug'] not in completed_slugs]

    is_final_test_granted = False
    can_take_final_test = True
    f_cooldown_hours = 0
    f_cooldown_minutes = 0
    submitted_lessons_count = 0
    all_lessons_submitted = False
    if request.user.is_authenticated:
        is_final_test_granted = profile.is_final_test_granted(selected_slug)
        can_take_final_test, f_cooldown_hours, f_cooldown_minutes = profile.can_take_final_test()
        submitted_lessons_set = set(HomeworkSubmission.objects.filter(user=request.user).values_list('lesson_id', flat=True))
        required_lessons_set = set(range(1, 11))
        submitted_lessons_count = len(submitted_lessons_set.intersection(required_lessons_set))
        all_lessons_submitted = required_lessons_set.issubset(submitted_lessons_set)

    context = {
        'courses': courses,
        'categories': categories,
        'video_library': video_library,
        'is_final_test_granted': is_final_test_granted,
        'can_take_final_test': can_take_final_test,
        'final_test_cooldown_hours': f_cooldown_hours,
        'final_test_cooldown_minutes': f_cooldown_minutes,
        'submitted_lessons_count': submitted_lessons_count,
        'all_lessons_submitted': all_lessons_submitted,
        'final_test_score': profile.final_test_score if request.user.is_authenticated else None,
        'current_section': current_section,
        'current_video': current_video,
        'selected_slug': selected_slug,
        'video_lessons': current_section['videos'],
        'is_superadmin': is_superadmin,
        'is_fully_unlocked': current_video_is_unlocked,
        'current_video_is_unlocked': current_video_is_unlocked,
        'unlocked_for_all': unlocked_for_all,
        'all_users': all_users,
        'user_homeworks': user_homeworks,
        'is_direction_completed': is_direction_completed,
        'user_direction': profile.direction,
        'user_direction_slug': direction_slug,
        'completed_slugs': completed_slugs,
        'current_note': current_note,
        'lesson_questions': lesson_questions,
        'user_certificate': user_certificate,
        'pending_direction_request': pending_direction_request,
        'available_next_directions': available_next_directions,
        'user_role': getattr(profile, 'role', 'student'),
    }
    return render(request, 'dashboard/videos.html', context)


def admin_unlock_videos_view(request):
    """
    Superadmin foydalanuvchilarga videolarni 90% tomosha qilmasdan
    ochib berish (qulfdan chiqarish) yoki qayta qulflash imkoniyati.
    """
    if not request.user.is_authenticated or not request.user.is_superuser:
        return JsonResponse({'success': False, 'error': 'Faqat Superadmin uchun ruxsat berilgan!'}, status=403)

    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body.decode('utf-8'))
            else:
                data = request.POST

            action = data.get('action', 'unlock_all')
            target_user_id = data.get('user_id')
            category_slug = data.get('category', 'all')

            if action == 'unlock_all':
                # Barcha foydalanuvchilar uchun hamma videolarni ochish
                UserVideoUnlock.objects.get_or_create(
                    unlocked_for_all_users=True,
                    category_slug='all',
                    defaults={'unlocked_by': request.user}
                )
                return JsonResponse({
                    'success': True,
                    'message': 'Barcha foydalanuvchilar uchun 90% talabisiz hamma videolar ochildi!'
                })

            elif action == 'unlock_user' and target_user_id:
                # Tanlangan foydalanuvchi uchun videolarni ochish
                target_user = get_object_or_404(User, id=target_user_id)
                UserVideoUnlock.objects.get_or_create(
                    user=target_user,
                    category_slug=category_slug,
                    defaults={'unlocked_by': request.user, 'unlocked_for_all_users': False}
                )
                return JsonResponse({
                    'success': True,
                    'message': f"Foydalanuvchi '{target_user.username}' uchun barcha videolar 90% talabisiz ochildi!"
                })

            elif action == 'relock_all':
                # Barcha ochilgan ruxsatlarni tozalash (qayta 90% qulfi yoqiladi)
                UserVideoUnlock.objects.all().delete()
                return JsonResponse({
                    'success': True,
                    'message': 'Barcha darslar qayta qulflandi. Endi 90% tomosha qilish talab qilinadi.'
                })

            return JsonResponse({'success': False, 'error': 'Noma\'lum amal'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Faqat POST so\'rovi qabul qilinadi'}, status=405)


def account_view(request):
    """Shaxsiy hisob (Account) bo'limi"""
    if not request.user.is_authenticated:
        return redirect('register')
    return render(request, 'dashboard/account.html', {'active_menu': 'account'})


@ensure_csrf_cookie
def typing_view(request):
    """Speed Typing (Tez Yozish O'yini) & Leaderboard bo'limi"""
    if not request.user.is_authenticated:
        return redirect('register')
    if not request.user.is_superuser:
        u_prof = getattr(request.user, 'profile', None)
        if u_prof and u_prof.role == 'student' and (not u_prof.is_approved or u_prof.approval_status != 'approved'):
            from django.contrib.auth import logout
            logout(request)
            messages.warning(request, "Ustoz taklifnomangizni qabul qilmaguncha tizimga kira olmaysiz.")
            return redirect('login')
    top_scores = list(TypingScore.objects.all()[:15])
    podium_scores = top_scores[:3] if len(top_scores) >= 3 else top_scores

    user_best = None
    user_games_count = 0
    user_avg_wpm = 0
    user_rank = None

    if request.user.is_authenticated:
        user_scores = TypingScore.objects.filter(user=request.user)
        user_best = user_scores.order_by('-wpm').first()
        user_games_count = user_scores.count()
        if user_best:
            user_rank = TypingScore.objects.filter(wpm__gt=user_best.wpm).count() + 1
            avg_res = user_scores.aggregate(Avg('wpm'))['wpm__avg']
            user_avg_wpm = round(avg_res) if avg_res else user_best.wpm

    context = {
        'active_menu': 'typing',
        'top_scores': top_scores,
        'podium_scores': podium_scores,
        'user_best': user_best,
        'user_games_count': user_games_count,
        'user_avg_wpm': user_avg_wpm,
        'user_rank': user_rank,
    }
    return render(request, 'dashboard/typing.html', context)


def typing_leaderboard_view(request):
    """Speed Typing Leaderboard (Peshqadamlar Jadvali) sahifasi"""
    if not request.user.is_authenticated:
        return redirect('register')
    mode = request.GET.get('mode', '').strip()
    time_limit = request.GET.get('time', '').strip()

    scores = TypingScore.objects.all()
    if mode in ['code', 'words']:
        scores = scores.filter(mode=mode)
    if time_limit and time_limit.isdigit():
        scores = scores.filter(time_limit=int(time_limit))

    top_scores = list(scores[:50])
    podium_scores = top_scores[:3] if len(top_scores) >= 3 else top_scores

    user_best = None
    user_rank = None
    if request.user.is_authenticated:
        user_best = TypingScore.objects.filter(user=request.user).first()
        if user_best:
            user_rank = TypingScore.objects.filter(wpm__gt=user_best.wpm).count() + 1

    total_games = TypingScore.objects.count()
    highest_score = TypingScore.objects.order_by('-wpm').first()
    highest_wpm = highest_score.wpm if highest_score else 0

    user_grades = HomeworkSubmission.objects.filter(user=request.user).order_by('-submitted_at')

    context = {
        'active_menu': 'leaderboard',
        'top_scores': top_scores,
        'podium_scores': podium_scores,
        'selected_mode': mode,
        'selected_time': time_limit,
        'user_best': user_best,
        'user_rank': user_rank,
        'total_games': total_games,
        'highest_wpm': highest_wpm,
        'user_grades': user_grades,
    }
    return render(request, 'dashboard/leaderboard.html', context)


def student_grades_view(request):
    """
    O'quvchining barcha topshirgan vazifalari va ustoz qo'ygan baholari sahifasi:
    - Qo'yilgan baho (0-100)
    - Ustoz izohi (feedback)
    - Qachon qo'yilgani (graded_at)
    - Qaysi yo'nalishdan (direction)
    - Dars nomi / raqami
    """
    if not request.user.is_authenticated:
        return redirect('register')

    submissions = HomeworkSubmission.objects.filter(user=request.user).order_by('-submitted_at')

    total_submitted = submissions.count()
    graded_count = submissions.filter(status='graded').count()
    pending_count = submissions.filter(status__in=['submitted', 'in_review']).count()

    graded_submissions = submissions.filter(status='graded', score__isnull=False)
    avg_score = graded_submissions.aggregate(Avg('score'))['score__avg'] or 0
    avg_score = round(avg_score, 1)

    context = {
        'active_menu': 'grades',
        'submissions': submissions,
        'total_submitted': total_submitted,
        'graded_count': graded_count,
        'pending_count': pending_count,
        'avg_score': avg_score,
    }
    return render(request, 'dashboard/grades.html', context)


def save_typing_score_view(request):
    """Speed Typing o'yini natijasini saqlash API (AJAX) — Real Personal Best & Recordboard"""
    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body.decode('utf-8'))
            else:
                data = request.POST

            wpm = int(data.get('wpm', 0))
            accuracy = int(data.get('accuracy', 100))
            mode = data.get('mode', 'code')
            time_limit = int(data.get('time_limit', 30))

            if wpm <= 0 or wpm > 300:
                return JsonResponse({'success': False, 'error': 'Noto\'g\'ri WPM qiymati'}, status=400)

            if request.user.is_authenticated:
                user = request.user
                player_name = user.first_name or user.username
                prev_best = TypingScore.objects.filter(user=user).order_by('-wpm').first()
            else:
                user = None
                player_name = data.get('player_name', '').strip() or "Koder"
                prev_best = TypingScore.objects.filter(player_name__iexact=player_name).order_by('-wpm').first()

            prev_best_wpm = prev_best.wpm if prev_best else 0
            is_new_record = (prev_best is None) or (wpm > prev_best_wpm)
            improvement = (wpm - prev_best_wpm) if (prev_best and wpm > prev_best_wpm) else 0

            score = TypingScore.objects.create(
                user=user,
                player_name=player_name,
                wpm=wpm,
                accuracy=accuracy,
                mode=mode,
                time_limit=time_limit
            )

            # Reytingdagi o'rni
            rank = TypingScore.objects.filter(wpm__gt=wpm).count() + 1

            # Foydalanuvchining umumiy statistikasi
            if user:
                user_scores = TypingScore.objects.filter(user=user)
            else:
                user_scores = TypingScore.objects.filter(player_name__iexact=player_name)

            total_games = user_scores.count()
            avg_res = user_scores.aggregate(Avg('wpm'))['wpm__avg']
            avg_wpm = round(avg_res) if avg_res else wpm
            personal_best = max(wpm, prev_best_wpm)

            # Yangilangan top 10 natijalar
            top_records = []
            for s in TypingScore.objects.all()[:10]:
                top_records.append({
                    'player_name': s.player_name,
                    'wpm': s.wpm,
                    'accuracy': s.accuracy,
                    'mode': s.mode,
                    'time_limit': s.time_limit
                })

            return JsonResponse({
                'success': True,
                'message': 'Natija Leaderboardga saqlandi!',
                'score_id': score.id,
                'player_name': player_name,
                'wpm': wpm,
                'accuracy': accuracy,
                'rank': rank,
                'is_new_record': is_new_record,
                'prev_best_wpm': prev_best_wpm,
                'improvement': improvement,
                'personal_best_wpm': personal_best,
                'total_games': total_games,
                'avg_wpm': avg_wpm,
                'top_scores': top_records
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Faqat POST qabul qilinadi'}, status=405)


def submit_homework_view(request):
    """Uy vazifasi (homework) topshirish API — AJAX POST"""
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': "Faqat POST qabul qilinadi"}, status=405)

    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'error': "Avval tizimga kiring!"}, status=401)

    try:
        category_slug = request.POST.get('category_slug', '').strip()
        lesson_id = int(request.POST.get('lesson_id', 1))
        text_content = request.POST.get('text_content', '').strip()
        github_link = request.POST.get('github_link', '').strip()
        uploaded_file = request.FILES.get('file')

        if not text_content and not github_link and not uploaded_file:
            return JsonResponse({
                'success': False,
                'error': "Kamida bitta: matn, GitHub havola yoki fayl yuklashingiz kerak!"
            }, status=400)

        # Videoni kamida 90% tomosha qilganlik tekshiruvi:
        watch_percent = 0
        try:
            watch_percent = int(request.POST.get('watch_percent', 0))
        except (ValueError, TypeError):
            watch_percent = 0

        if not request.user.is_superuser:
            unlocked_for_all = UserVideoUnlock.objects.filter(unlocked_for_all_users=True, category_slug__in=['all', category_slug]).exists()
            user_unlocked = UserVideoUnlock.objects.filter(user=request.user, category_slug__in=['all', category_slug], lesson_id__in=[0, lesson_id]).exists()
            if not unlocked_for_all and not user_unlocked and watch_percent < 90:
                return JsonResponse({
                    'success': False,
                    'error': f"Siz ushbu videoni kamida 90% tomosha qilishingiz shart! Hozirgi natijangiz: {watch_percent}%. Videoni ko'rib bo'lgach, vazifani topshiring."
                }, status=400)

        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        student_name = request.user.first_name or request.user.username
        group_name = profile.group_name or "FN-24"
        direction = profile.direction or category_slug.replace('-', ' ').title()

        submission = HomeworkSubmission.objects.create(
            user=request.user,
            student_name=student_name,
            group_name=group_name,
            direction=direction,
            category_slug=category_slug,
            lesson_id=lesson_id,
            text_content=text_content,
            github_link=github_link,
            file=uploaded_file,
            status='submitted'
        )

        # Teacher va superadminlarga tizim bildirishnomasi (Notification) yuborish
        try:
            teachers = User.objects.filter(
                Q(is_superuser=True) | Q(profile__role='teacher') | Q(username='rixsi')
            ).distinct()
            for teacher in teachers:
                Notification.objects.create(
                    user=teacher,
                    title=f"📝 Yangi vazifa: {student_name}",
                    message=f"{student_name} ({group_name}) — {direction} {lesson_id}-dars vazifasini topshirdi.",
                    link="/courses/teacher/?tab=homeworks",
                    icon="file-signature"
                )
        except Exception as notif_err:
            pass

        # Telegram xabarnomasi
        send_telegram_bot_message(
            f"📝 <b>Yangi Uy Vazifasi Topshirildi!</b>\n\n"
            f"👤 <b>Talaba:</b> {student_name} (Guruh: {group_name})\n"
            f"📚 <b>Kurs:</b> {direction} (Dars #{lesson_id})\n"
            f"🔗 <b>GitHub / Demo:</b> {github_link or 'Fayl/Matn yuborildi'}\n"
            f"🕐 <b>Vaqt:</b> {submission.submitted_at.strftime('%d.%m.%Y %H:%M')}\n\n"
            f"👨‍🏫 <i>Ustoz LMS da tekshirish kutilmoqda</i>"
        )

        return JsonResponse({
            'success': True,
            'message': f"Vazifa muvaffaqiyatli topshirildi! (#{submission.id}) O'qituvchi tekshirib baholaydi.",
            'submission_id': submission.id,
            'student_name': student_name,
            'group_name': group_name,
            'direction': direction,
            'submitted_at': submission.submitted_at.strftime('%d.%m.%Y %H:%M')
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


def billing_view(request):
    """Billing to'lovlar tarixi"""
    if not request.user.is_authenticated:
        return redirect('register')
    return render(request, 'dashboard/billing.html', {'active_menu': 'billing'})


def usage_view(request):
    """Usage o'quv faolligi"""
    if not request.user.is_authenticated:
        return redirect('register')
    return render(request, 'dashboard/usage.html', {'active_menu': 'usage'})


def register_view(request):
    """
    Foydalanuvchi ro'yxatdan o'tishi:
    1-Bosqich: Foydalanuvchi ism va emailini kiritib Enter bosadi.
    2-Bosqich: Ekranda @computer12super_bot botiga o'tish ko'rsatiladi va botdagi parol so'raladi.
    3-Bosqich: Foydalanuvchi botdan olgan parolni kiritadi va taklifnoma o'qituvchiga yuboriladi.
    O'qituvchi qabul qilgandan so'ng foydalanuvchi tizimga kira oladi.
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        is_ajax = (
            request.headers.get('x-requested-with') == 'XMLHttpRequest' or
            request.content_type == 'application/json' or
            request.POST.get('ajax') == '1'
        )

        step = str(request.POST.get('step', '1')).strip()

        # ---------------------------------------------------------------------
        # 1-BOSQICH: Ism va Email kiritish -> Botga yo'naltirish
        # ---------------------------------------------------------------------
        if step == '1':
            full_name = request.POST.get('full_name', '').strip()
            email = request.POST.get('email', '').strip().lower()
            telegram_username = request.POST.get('telegram_username', '').strip().lstrip('@').lower()
            group_name = "Guruhsiz"  # guruhni faqat ustoz belgilaydi
            direction = request.POST.get('direction', '').strip() or "Python Backend"

            errors = []
            if not telegram_username:
                errors.append("Iltimos, Telegram foydalanuvchi nomingizni (@username) kiriting.")
            elif len(telegram_username) < 3:
                errors.append("Telegram username kamida 3 ta belgidan iborat bo'lishi kerak.")
            if not full_name:
                errors.append("Iltimos, to'liq ismingizni kiriting.")
            elif len(full_name) < 2:
                errors.append("Ism kamida 2 ta belgidan iborat bo'lishi kerak.")

            email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if not email:
                errors.append("Iltimos, elektron pochtangizni kiriting.")
            elif not re.match(email_regex, email):
                errors.append("Noto'g'ri elektron pochta formati (masalan: talaba@gmail.com).")

            existing_user = User.objects.filter(email__iexact=email).first()
            if existing_user:
                profile = getattr(existing_user, 'profile', None)
                if profile and profile.is_approved:
                    errors.append("Ushbu elektron pochta orqali allaqachon ro'yxatdan o'tilgan. Iltimos, tizimga kiring.")

            if errors:
                total_students = User.objects.filter(is_superuser=False).count()
                if is_ajax:
                    return JsonResponse({'success': False, 'errors': errors}, status=400)
                for err in errors:
                    messages.error(request, err)
                return render(request, 'register.html', {
                    'full_name': full_name,
                    'email': email,
                    'total_students': total_students,
                })

            # 6 xonali tasdiqlash paroli generatsiya qilish
            generated_password = str(random.randint(100000, 999999))

            if existing_user:
                user = existing_user
                user.first_name = full_name
                user.set_password(generated_password)
                user.is_active = False
                user.save()
                profile, _ = UserProfile.objects.get_or_create(user=user)
                profile.group_name = group_name
                profile.direction = direction
                profile.telegram_username = telegram_username
                profile.telegram_auth_code = generated_password
                profile.plain_password = generated_password
                profile.approval_status = 'pending_telegram'
                profile.is_approved = False
                profile.telegram_code_verified = False
                profile.save()
            else:
                base_username = re.sub(r'[^a-zA-Z0-9_]', '', email.split('@')[0]) or 'student'
                username = base_username
                counter = 1
                while User.objects.filter(username__iexact=username).exists():
                    username = f"{base_username}{counter}"
                    counter += 1

                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=generated_password,
                    first_name=full_name,
                    is_active=False
                )
                user.save()

                profile = UserProfile.objects.create(
                    user=user,
                    role='student',
                    group_name=group_name,
                    direction=direction,
                    telegram_username=telegram_username,
                    is_approved=False,
                    approval_status='pending_telegram',
                    telegram_auth_code=generated_password,
                    plain_password=generated_password,
                    telegram_code_verified=False
                )

            # Ustoz / Botga xabarnoma yuborish
            now = timezone.now().strftime('%d.%m.%Y %H:%M:%S')
            send_telegram_raw_message(
                TEACHER_CHAT_ID,
                f"🆕 <b>Yangi talaba ro'yxatdan o'tmoqda!</b>\n\n"
                f"👤 <b>Ism:</b> {full_name}\n"
                f"📧 <b>Email:</b> {email}\n"
                f"📚 <b>Yo'nalish:</b> {direction}\n"
                f"🔐 <b>Bot uchun parol:</b> <code>{generated_password}</code>\n"
                f"🕐 <b>Vaqt:</b> {now}"
            )

            bot_url = f"https://t.me/{TELEGRAM_BOT_USERNAME}?start=auth_{user.id}"

            if is_ajax:
                return JsonResponse({
                    'success': True,
                    'step': 2,
                    'user_id': user.id,
                    'email': email,
                    'full_name': full_name,
                    'bot_username': TELEGRAM_BOT_USERNAME,
                    'bot_url': bot_url,
                    'message': f"Iltimos, @{TELEGRAM_BOT_USERNAME} Telegram botimizga o'ting va /start bosing!"
                })

            return render(request, 'register.html', {
                'step': 2,
                'user_id': user.id,
                'email': email,
                'full_name': full_name,
                'bot_username': TELEGRAM_BOT_USERNAME,
                'bot_url': bot_url,
                'total_students': User.objects.filter(is_superuser=False).count(),
            })

        # ---------------------------------------------------------------------
        # 2-BOSQICH: Botdan olingan parolni tasdiqlash -> Taklifnoma ustozga yuboriladi
        # ---------------------------------------------------------------------
        elif step == '2':
            email = request.POST.get('email', '').strip().lower()
            password_input = request.POST.get('password', '').strip()

            if not email or not password_input:
                err_msg = "Elektron pochta va Telegram botdan olingan parolni kiriting."
                if is_ajax:
                    return JsonResponse({'success': False, 'errors': [err_msg]}, status=400)
                messages.error(request, err_msg)
                return redirect('register')

            user = User.objects.filter(email__iexact=email).first()
            if not user or not hasattr(user, 'profile'):
                err_msg = "Bunday foydalanuvchi ro'yxati topilmadi. Qaytadan urinib ko'ring."
                if is_ajax:
                    return JsonResponse({'success': False, 'errors': [err_msg]}, status=404)
                messages.error(request, err_msg)
                return redirect('register')

            profile = user.profile
            is_valid = (
                user.check_password(password_input) or
                (profile.telegram_auth_code and profile.telegram_auth_code.strip() == password_input)
            )

            if not is_valid:
                err_msg = f"Kiritilgan parol noto'g'ri! Iltimos, @{TELEGRAM_BOT_USERNAME} botidagi xabarni tekshirib qayta kiriting."
                if is_ajax:
                    return JsonResponse({'success': False, 'errors': [err_msg]}, status=400)
                messages.error(request, err_msg)
                return render(request, 'register.html', {
                    'step': 2,
                    'email': email,
                    'full_name': user.first_name,
                    'bot_username': TELEGRAM_BOT_USERNAME,
                    'bot_url': f"https://t.me/{TELEGRAM_BOT_USERNAME}?start=auth_{user.id}",
                })

            # Parol to'g'ri kiritildi! Endi taklifnoma o'qituvchiga yuboriladi!
            profile.telegram_code_verified = True
            profile.approval_status = 'pending_teacher'
            profile.is_approved = False
            profile.save()

            # O'qituvchiga taklifnoma yuborish
            notify_teacher_new_request(user, profile)

            success_msg = (
                f"Parol muvaffaqiyatli tasdiqlandi! "
                f"Sizning taklifnomangiz (priglasheniya) o'qituvchiga yuborildi. "
                f"O'qituvchi sizni qabul qilgandan so'ng tizimga to'liq kira olasiz!"
            )

            if is_ajax:
                return JsonResponse({
                    'success': True,
                    'step': 3,
                    'status': 'pending_teacher',
                    'message': success_msg,
                    'full_name': user.first_name,
                    'email': email,
                })

            messages.success(request, success_msg)
            return render(request, 'register.html', {
                'step': 3,
                'email': email,
                'full_name': user.first_name,
                'success_message': success_msg
            })

    total_students = User.objects.filter(is_superuser=False).count()
    return render(request, 'register.html', {
        'total_students': total_students,
        'step': 1,
        'bot_username': TELEGRAM_BOT_USERNAME,
    })


def check_student_approval_api(request):
    """
    Talabaning o'qituvchi tomonidan tasdiqlanganlik holatini tekshirish API si.
    Ustoz qabul qilganda eski o'qituvchi (rixsi) sessiyasi chiqarilib,
    aynan o'sha yangi ro'yxatdan o'tgan o'quvchining o'zi login qilinadi!
    """
    email = request.GET.get('email', '').strip().lower()
    if not email:
        return JsonResponse({'success': False, 'message': "Email kiritilmadi"}, status=400)

    user = User.objects.filter(email__iexact=email).first()
    if not user or not hasattr(user, 'profile'):
        return JsonResponse({'success': False, 'message': "Foydalanuvchi topilmadi"}, status=404)

    profile = user.profile

    # Agar ustoz talabani qabul qilgan bo'lsa:
    if profile.is_approved and profile.approval_status == 'approved':
        # Agar sessiyada eski user (masalan rixsi ustoz) kirgan bo'lsa, tozalaymiz
        if request.user.is_authenticated and request.user != user:
            auth_logout(request)

        # Aynan ro'yxatdan o'tgan o'quvchini sessiyaga login qilamiz!
        user.is_active = True
        user.save(update_fields=['is_active'])
        auth_login(request, user)

        return JsonResponse({
            'success': True,
            'is_approved': True,
            'approval_status': profile.approval_status,
            'first_name': user.first_name or user.username,
            'login': user.username,
            'email': user.email,
            'redirect_url': '/videos/'
        })

    return JsonResponse({
        'success': True,
        'is_approved': profile.is_approved,
        'approval_status': profile.approval_status,
        'first_name': user.first_name or user.username,
        'login': user.username,
        'email': user.email
    })


def teacher_approve_student_api(request):
    """
    O'qituvchi yangi ro'yxatdan o'tgan o'quvchi taklifnomasini qabul qilish yoki rad etish API si.
    """
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'message': "Avtorizatsiyadan o'tilmagan"}, status=401)

    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.user.username != 'rixsi' and not request.user.is_superuser and profile.role != 'teacher':
        return JsonResponse({'success': False, 'message': "Ruxsat etilmagan"}, status=403)

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        action = request.POST.get('action', 'approve') # 'approve' yoki 'reject'

        student_user = get_object_or_404(User, id=student_id)
        student_profile, _ = UserProfile.objects.get_or_create(user=student_user)

        if action == 'approve':
            custom_username = request.POST.get('custom_username', '').strip()
            custom_password = request.POST.get('custom_password', '').strip()
            custom_group = request.POST.get('custom_group', '').strip()

            if not custom_group:
                return JsonResponse({'success': False, 'message': "Iltimos, o'quvchi uchun guruhni belgilang"}, status=400)

            if custom_username:
                existing = User.objects.filter(username__iexact=custom_username).exclude(id=student_user.id).first()
                if not existing:
                    student_user.username = custom_username

            if custom_password:
                student_user.set_password(custom_password)
                student_profile.telegram_auth_code = custom_password
                student_profile.plain_password = custom_password

            student_user.is_active = True
            student_user.save()

            student_profile.is_approved = True
            student_profile.approval_status = 'approved'
            student_profile.group_name = custom_group
            student_profile.save(update_fields=['is_approved', 'approval_status', 'telegram_auth_code', 'plain_password', 'group_name'])

            login_used = student_user.username
            password_used = custom_password or student_profile.telegram_auth_code or "123456"

            # Talabaning Telegram botiga xushxabar (ustoz bergan login va parol bilan) yuborish
            notify_student_approved(student_user, student_profile, login=login_used, password=password_used)

            return JsonResponse({
                'success': True,
                'status': 'approved',
                'login': login_used,
                'password': password_used,
                'message': f"O'quvchi {student_user.first_name or student_user.username} QABUL QILINDI! Login: {login_used}, Parol: {password_used}. Talabaga bot orqali xabar yuborildi."
            })
        elif action == 'reject':
            student_user.is_active = False
            student_user.save(update_fields=['is_active'])

            student_profile.is_approved = False
            student_profile.approval_status = 'rejected'
            student_profile.save(update_fields=['is_approved', 'approval_status'])

            # Talabaga rad etilganlik xabari
            notify_student_rejected(student_user, student_profile)

            return JsonResponse({
                'success': True,
                'status': 'rejected',
                'message': f"O'quvchi {student_user.first_name or student_user.username} ning taklifnomasi rad etildi."
            })

    return JsonResponse({'success': False, 'message': "Noto'g'ri so'rov"}, status=400)


def login_view(request):
    """
    Foydalanuvchi tizimga kirishi:
    - Login va parol orqali kirish.
    - O'qituvchi tomonidan qabul qilinganlik holatini tekshiradi.
    """
    # Agar yangi talaba ro'yxatdan o'tgan bo'lsa yoki URL da parametr bo'lsa:
    # Eski sessiyadagi o'qituvchi (rixsi) ni tozalaymiz, toki talaba platformasiga ustoz kirib ketmasin!
    if request.GET.get('registered') == '1' or request.GET.get('login') or request.GET.get('email'):
        if request.user.is_authenticated:
            auth_logout(request)

    # Agar allaqachon login qilingan bo'lsa:
    if request.user.is_authenticated:
        if request.user.username == 'rixsi' or getattr(getattr(request.user, 'profile', None), 'role', '') == 'teacher':
            return redirect('teacher_dashboard')
        return redirect('videos')

    registered_login = request.GET.get('login', '').strip() or request.GET.get('username', '').strip() or request.GET.get('email', '').strip()
    was_registered = request.GET.get('registered') == '1'

    if request.method == 'POST':
        login_input = request.POST.get('login_input', '').strip()
        password = request.POST.get('password', '')
        remember_me = request.POST.get('remember_me')

        if not login_input or not password:
            messages.error(request, "Iltimos, login va parolingizni kiriting.")
            return render(request, 'login.html', {'login_input': login_input})

        # Username yoki email orqali foydalanuvchini topish
        user_obj = User.objects.filter(Q(username__iexact=login_input) | Q(email__iexact=login_input)).first()

        if not user_obj:
            messages.error(request, "Login yoki parol noto'g'ri kiritildi.")
            return render(request, 'login.html', {'login_input': login_input})

        # Parolni tekshirish
        is_password_correct = user_obj.check_password(password)
        if not is_password_correct:
            messages.error(request, "Login yoki parol noto'g'ri kiritildi.")
            return render(request, 'login.html', {'login_input': login_input})

        # Foydalanuvchi profilini tekshirish
        profile, _ = UserProfile.objects.get_or_create(user=user_obj)

        # Agar admin yoki o'qituvchi bo'lsa teacher_dashboard ga
        if user_obj.is_superuser or user_obj.username == 'rixsi' or profile.role == 'teacher':
            user_obj.is_active = True
            user_obj.save(update_fields=['is_active'])
            auth_login(request, user_obj)
            messages.success(request, f"Xush kelibsiz, {user_obj.first_name or user_obj.username}!")
            return redirect('teacher_dashboard')

        # O'quvchi tasdiqlanganmi?
        if not profile.is_approved or profile.approval_status != 'approved':
            if profile.approval_status == 'pending_telegram':
                messages.warning(
                    request,
                    f"⚠️ Siz hali ro'yxatdan o'tishni yakunlamagansiz! Iltimos, Telegram'dagi @{TELEGRAM_BOT_USERNAME} botiga o'tib parolni tasdiqlang."
                )
            elif profile.approval_status == 'rejected':
                messages.error(
                    request,
                    "❌ Afsuski, sizning platformaga a'zolik taklifnomangiz o'qituvchi tomonidan rad etilgan."
                )
            else:
                messages.info(
                    request,
                    f"⏳ Hurmatli {user_obj.first_name or user_obj.username}! Sizning a'zolik taklifnomangiz hali o'qituvchi tomonidan ko'rib chiqilmoqda. Ustoz sizni qabul qilgandan so'ng darhol tizimga kira olasiz!"
                )
            return render(request, 'login.html', {
                'login_input': login_input,
                'is_pending_approval': True,
                'student_name': user_obj.first_name or user_obj.username
            })

        # O'quvchi muvaffaqiyatli qabul qilingan — Tizimga kiritish!
        user_obj.is_active = True
        user_obj.save(update_fields=['is_active'])
        auth_login(request, user_obj)

        if not remember_me:
            request.session.set_expiry(0)
        else:
            request.session.set_expiry(1209600)

        messages.success(request, f"Xush kelibsiz, {user_obj.first_name or user_obj.username}!")
        next_url = request.GET.get('next', 'videos')
        return redirect(next_url)

    return render(request, 'login.html', {
        'login_input': registered_login,
        'was_registered': was_registered,
    })


def logout_view(request):
    """Tizimdan chiqish"""
    auth_logout(request)
    messages.info(request, "Tizimdan muvaffaqiyatli chiqdingiz.")
    return redirect('login')


# ============================================================================
# TEACHER & ADMIN LMS PLATFORMASI
# ============================================================================

def teacher_login_view(request):
    """
    Teacher & Admin Portal Maxsus Kirish Sahifasi:
    Faqat Ustoz va Adminlar uchun (Login: rixsi, Parol: 123456)
    """
    if request.user.is_authenticated:
        if request.user.username == 'rixsi' or request.user.is_superuser or getattr(request.user, 'profile', None) and request.user.profile.role == 'teacher':
            return redirect('teacher_dashboard')

    if request.method == 'POST':
        login_input = request.POST.get('login_input', '').strip()
        password = request.POST.get('password', '')

        if not login_input or not password:
            messages.error(request, "Iltimos, ustoz login va parolingizni kiriting.")
            return render(request, 'dashboard/teacher_login.html', {'login_input': login_input})

        user_obj = User.objects.filter(Q(username__iexact=login_input) | Q(email__iexact=login_input)).first()
        user = None
        if user_obj:
            user = authenticate(request, username=user_obj.username, password=password)

        if user is not None:
            # Agar rixsi bo'lsa yoki admin/teacher bo'lsa ruxsat beramiz
            profile, _ = UserProfile.objects.get_or_create(user=user)
            if user.username == 'rixsi' or user.is_superuser or user.is_staff or profile.role in ['teacher', 'admin']:
                profile.role = 'teacher'
                profile.save()
                auth_login(request, user)
                messages.success(request, f"Xush kelibsiz, Ustoz {user.first_name or user.username}!")
                return redirect('teacher_dashboard')
            else:
                messages.error(request, "Ushbu hisob bilan faqat o'quvchi sifatida kirish mumkin. Teacher huquqi mavjud emas.")
                return render(request, 'dashboard/teacher_login.html', {'login_input': login_input})
        else:
            messages.error(request, "Login yoki parol noto'g'ri kiritildi! (Ustoz login: rixsi, parol: 123456)")
            return render(request, 'dashboard/teacher_login.html', {'login_input': login_input})

    return render(request, 'dashboard/teacher_login.html')


def teacher_logout_view(request):
    """Teacher portaldan chiqish"""
    auth_logout(request)
    messages.info(request, "Teacher paneldan muvaffaqiyatli chiqdingiz.")
    return redirect('teacher_login')


def teacher_dashboard_view(request):
    """
    Teacher & Admin LMS Boshqaruv Markazi:
    - Login: rixsi, Parol: 123456
    - Kategoriyalar (Category) bo'yicha qaysi o'quvchiga qaysi videoni ochish
    - O'quvchilarga darslarni ochib berish va qayta qulflash
    - Barcha uy vazifalarini tekshirib 0-100 ball qo'yish
    """
    if not request.user.is_authenticated:
        return redirect('teacher_login')

    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.user.username != 'rixsi' and not request.user.is_superuser and profile.role != 'teacher':
        return redirect('teacher_login')

    # Filtrlash va qidiruv parametrlari
    search_q = request.GET.get('q', '').strip()
    selected_group = request.GET.get('group', '').strip()
    selected_category = request.GET.get('cat', '').strip()
    status_filter = request.GET.get('status', '').strip()

    # Barcha o'quvchilar ro'yxati (oddiy userlar)
    students_query = User.objects.filter(is_superuser=False).select_related('profile').order_by('-date_joined')
    if search_q:
        students_query = students_query.filter(
            Q(first_name__icontains=search_q) |
            Q(username__icontains=search_q) |
            Q(email__icontains=search_q)
        )
    if selected_group:
        students_query = students_query.filter(profile__group_name=selected_group)

    students_data = []
    for s in students_query:
        sp, _ = UserProfile.objects.get_or_create(user=s)
        unlocks = list(UserVideoUnlock.objects.filter(user=s))
        hw_count = HomeworkSubmission.objects.filter(user=s).count()
        graded_count = HomeworkSubmission.objects.filter(user=s, status='graded').count()
        total_lessons = 10
        progress_percentage = min(100, round((graded_count / total_lessons) * 100))
        students_data.append({
            'user': s,
            'profile': sp,
            'unlocks': unlocks,
            'unlocks_count': len(unlocks),
            'hw_count': hw_count,
            'graded_count': graded_count,
            'total_lessons': total_lessons,
            'progress_percentage': progress_percentage,
        })

    # Barcha topshirilgan uy vazifalari (Homeworks)
    homeworks = HomeworkSubmission.objects.all().select_related('user').order_by('-submitted_at')
    if status_filter:
        homeworks = homeworks.filter(status=status_filter)
    if search_q:
        homeworks = homeworks.filter(
            Q(student_name__icontains=search_q) |
            Q(group_name__icontains=search_q) |
            Q(direction__icontains=search_q) |
            Q(user__username__icontains=search_q)
        )
    if selected_group:
        homeworks = homeworks.filter(group_name=selected_group)

    # Statistika
    total_students = User.objects.filter(is_superuser=False).count()
    total_submissions = HomeworkSubmission.objects.count()
    pending_submissions = HomeworkSubmission.objects.filter(status='submitted').count()
    graded_submissions = HomeworkSubmission.objects.filter(status='graded').count()
    total_unlocks = UserVideoUnlock.objects.count()

    # Mavjud guruhlar ro'yxati
    available_groups = [g for g in UserProfile.objects.values_list('group_name', flat=True).distinct() if g != 'Guruhsiz']
    if not available_groups:
        available_groups = ['FN-24', 'PY-101', 'WEB-05', 'AI-02']

    # KATEGORIYALAR VA VIDEOLAR RO'YXATI (Teacher Video Unlocker uchun)
    categories_catalog = [
        {
            'slug': 'python-backend',
            'name': 'Python & Backend',
            'icon': 'server',
            'color': '#a855f7',
            'videos': [
                {'id': 1, 'title': "1-Dars: Python Full Course for Beginners [2024]", 'duration': '6:14:00'},
                {'id': 2, 'title': "2-Dars: Python Django Web Framework — Full Course", 'duration': '3:45:00'},
                {'id': 3, 'title': "3-Dars: Python Programming & REST API — Full Course", 'duration': '4:26:00'},
            ]
        },
        {
            'slug': 'web-dasturlash',
            'name': 'Veb Dasturlash',
            'icon': 'laptop-code',
            'color': '#38bdf8',
            'videos': [
                {'id': 1, 'title': "1-Dars: HTML Full Course — Build a Website", 'duration': '2:02:00'},
                {'id': 2, 'title': "2-Dars: JavaScript Full Course for Beginners", 'duration': '3:26:00'},
                {'id': 3, 'title': "3-Dars: React Course — Beginner's Tutorial for React", 'duration': '11:55:00'},
            ]
        },
        {
            'slug': 'ai-data-science',
            'name': "Sun'iy Intellekt & Data Science",
            'icon': 'brain',
            'color': '#34d399',
            'videos': [
                {'id': 1, 'title': "1-Dars: Machine Learning for Beginners — Full Course", 'duration': '9:52:00'},
                {'id': 2, 'title': "2-Dars: But what is a neural network? — Deep Learning", 'duration': '19:13'},
                {'id': 3, 'title': "3-Dars: Data Science Full Course for Beginners", 'duration': '5:30:00'},
            ]
        },
        {
            'slug': 'mobile-dev',
            'name': 'Mobil Dasturlash (Flutter)',
            'icon': 'mobile-screen',
            'color': '#06b6d4',
            'videos': [
                {'id': 1, 'title': "1-Dars: Flutter Course for Beginners — 37-hour Full Course", 'duration': '37:00:00'},
                {'id': 2, 'title': "2-Dars: Flutter & Dart — Full Tutorial for Beginners", 'duration': '3:10:00'},
                {'id': 3, 'title': "3-Dars: React Native Tutorial for Beginners", 'duration': '2:06:00'},
            ]
        },
        {
            'slug': 'ui-ux-design',
            'name': 'UI/UX Dizayn',
            'icon': 'palette',
            'color': '#f59e0b',
            'videos': [
                {'id': 1, 'title': "1-Dars: Figma UI Design Tutorial — Full Course", 'duration': '3:26:00'},
                {'id': 2, 'title': "2-Dars: UX Design Course — Learn User Experience", 'duration': '2:20:00'},
                {'id': 3, 'title': "3-Dars: Web Design for Beginners — Full Course", 'duration': '4:15:00'},
            ]
        },
        {
            'slug': 'kiberxavfsizlik',
            'name': 'Kiberxavfsizlik',
            'icon': 'shield-halved',
            'color': '#ef4444',
            'videos': [
                {'id': 1, 'title': "1-Dars: Introduction to IT & Cyber Security", 'duration': '4:20:00'},
                {'id': 2, 'title': "2-Dars: What Is Ethical Hacking & Cybersecurity", 'duration': '1:12:00'},
                {'id': 3, 'title': "3-Dars: OSINT & Cybersecurity Analysis in 90 Minutes", 'duration': '1:34:00'},
            ]
        },
    ]

    # O'quvchilar tomonidan berilgan savollar (Q&A)
    all_questions = LessonQuestion.objects.select_related('user', 'answered_by').order_by('-created_at')
    
    # E'lonlar ro'yxati
    announcements_list = Announcement.objects.select_related('author').order_by('-created_at')

    # Ro'yxatdan o'tgan yangi taklifnomalar (So'rovlar)
    pending_approval_students = User.objects.filter(
        is_superuser=False
    ).select_related('profile').filter(
        Q(profile__approval_status='pending_teacher') |
        Q(profile__approval_status='pending_telegram') |
        Q(profile__is_approved=False)
    ).order_by('-date_joined')
    pending_approval_count = pending_approval_students.filter(profile__approval_status='pending_teacher').count()

    # Yangi Yo'nalish Tanlash Taklifnomalari (Priglasheniyalar)
    direction_change_requests = DirectionChangeRequest.objects.filter(status='pending').select_related('user').order_by('-created_at')

    context = {
        'active_menu': 'teacher',
        'profile': profile,
        'students_data': students_data,
        'homeworks': homeworks,
        'pending_approval_students': pending_approval_students,
        'pending_approval_count': pending_approval_count,
        'direction_change_requests': direction_change_requests,
        'direction_change_count': direction_change_requests.count(),
        'total_students': total_students,
        'total_submissions': total_submissions,
        'pending_submissions': pending_submissions,
        'graded_submissions': graded_submissions,
        'total_unlocks': total_unlocks,
        'available_groups': available_groups,
        'categories_catalog': categories_catalog,
        'search_q': search_q,
        'selected_group': selected_group,
        'selected_category': selected_category,
        'status_filter': status_filter,
        'all_questions': all_questions,
        'announcements_list': announcements_list,
    }
    return render(request, 'dashboard/teacher.html', context)


def teacher_unlock_lesson_view(request):
    """
    Teacher / Admin tomonidan istalgan o'quvchiga dars ochib berish API (AJAX POST)
    """
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'error': 'Avval tizimga kiring!'}, status=401)

    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Faqat POST so\'rovi qabul qilinadi'}, status=405)

    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body.decode('utf-8'))
        else:
            data = request.POST

        target_user_id = data.get('user_id')
        target_group = data.get('target_group')
        category_slug = data.get('category_slug', 'all')
        lesson_id = int(data.get('lesson_id', 0))
        action = data.get('action', 'unlock')

        # 1. Agar butun bir guruh uchun ochilayotgan bo'lsa (masalan: FN-24)
        if target_group and target_group not in ['all', '']:
            group_users = User.objects.filter(profile__group_name=target_group)
            for gu in group_users:
                if action == 'unlock':
                    UserVideoUnlock.objects.get_or_create(
                        user=gu,
                        category_slug=category_slug,
                        lesson_id=lesson_id,
                        defaults={'unlocked_by': request.user}
                    )
                else:
                    if category_slug == 'all' and lesson_id == 0:
                        UserVideoUnlock.objects.filter(user=gu).delete()
                    else:
                        UserVideoUnlock.objects.filter(user=gu, category_slug=category_slug, lesson_id=lesson_id).delete()

            act_text = "ochildi! 🚀" if action == 'unlock' else "qulflandi."
            lesson_txt = "barcha darslar" if lesson_id == 0 else f"{lesson_id}-dars"
            return JsonResponse({
                'success': True,
                'message': f"'{target_group}' guruhi o'quvchilari uchun {category_slug} ({lesson_txt}) {act_text}"
            })

        # 2. Agar barcha o'quvchilar uchun bo'lsa
        if target_user_id == 'all' or not target_user_id:
            cat_name = "barcha yo'nalishlar" if category_slug == 'all' else category_slug
            lesson_txt = "hamma darslar" if lesson_id == 0 else f"{lesson_id}-dars"

            if action == 'unlock':
                UserVideoUnlock.objects.get_or_create(
                    unlocked_for_all_users=True,
                    category_slug=category_slug,
                    lesson_id=lesson_id,
                    defaults={'unlocked_by': request.user}
                )
                return JsonResponse({'success': True, 'message': f"Barcha o'quvchilar uchun {cat_name} ({lesson_txt}) ochildi! 🚀"})
            else:
                if category_slug == 'all' and lesson_id == 0:
                    UserVideoUnlock.objects.filter(unlocked_for_all_users=True).delete()
                else:
                    UserVideoUnlock.objects.filter(unlocked_for_all_users=True, category_slug=category_slug, lesson_id=lesson_id).delete()
                return JsonResponse({'success': True, 'message': f"Barcha o'quvchilar uchun {cat_name} ({lesson_txt}) qayta qulflandi."})

        target_user = get_object_or_404(User, id=target_user_id)

        if action == 'unlock':
            unlock_obj, created = UserVideoUnlock.objects.get_or_create(
                user=target_user,
                category_slug=category_slug,
                lesson_id=lesson_id,
                defaults={'unlocked_by': request.user, 'unlocked_for_all_users': False}
            )
            cat_name = "barcha yo'nalishlar" if category_slug == 'all' else category_slug
            lesson_txt = "hamma darslar" if lesson_id == 0 else f"{lesson_id}-dars"
            msg = f"O'quvchi '{target_user.first_name or target_user.username}' uchun {cat_name} ({lesson_txt}) ochildi! 🚀"
            return JsonResponse({'success': True, 'message': msg, 'status': 'unlocked'})

        elif action == 'relock':
            if category_slug == 'all' and lesson_id == 0:
                UserVideoUnlock.objects.filter(user=target_user).delete()
            else:
                UserVideoUnlock.objects.filter(user=target_user, category_slug=category_slug, lesson_id=lesson_id).delete()
            return JsonResponse({
                'success': True,
                'message': f"O'quvchi '{target_user.first_name or target_user.username}' uchun dars qayta qulflandi.",
                'status': 'relocked'
            })

        return JsonResponse({'success': False, 'error': 'Noma\'lum amal'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


def teacher_grant_final_test_view(request):
    """
    Teacher o'quvchiga yo'nalish bo'yicha yakuniy testni beradi.
    MUHIM: O'quvchi barcha 3 ta darsni tugatmaguncha yakuniy test berib bo'lmaydi!
    """
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'error': 'Avval tizimga kiring!'}, status=401)

    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.user.username != 'rixsi' and not request.user.is_superuser and profile.role != 'teacher':
        return JsonResponse({'success': False, 'error': 'Ruxsat etilmagan'}, status=403)

    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': "Faqat POST so'rovi qabul qilinadi"}, status=405)

    try:
        data = json.loads(request.body.decode('utf-8'))
        student = get_object_or_404(User, id=data.get('user_id'))
        category_slug = data.get('category_slug', '').strip()
        student_profile, _ = UserProfile.objects.get_or_create(user=student)
        if not category_slug:
            category_slug = student_profile.get_direction_slug()

        # O'quvchi barcha 10 ta darsni tugatganmi tekshiramiz
        required_lessons_set = set(range(1, 11))
        submitted_lessons = set(HomeworkSubmission.objects.filter(user=student).values_list('lesson_id', flat=True))
        if not required_lessons_set.issubset(submitted_lessons):
            missing = [str(l) for l in sorted(required_lessons_set - submitted_lessons)]
            return JsonResponse({
                'success': False,
                'error': f"O'quvchi hali barcha darslarni tugatmagan! {', '.join(missing)}-dars topshiriqlari topshirilmagan ({len(submitted_lessons.intersection(required_lessons_set))}/10 dars). O'quvchi barcha 10 ta darsni tugatmaguncha yakuniy test bera olmaysiz."
            }, status=400)

        student_profile.grant_final_test(category_slug)

        Notification.objects.create(
            user=student,
            title="Yakuniy test berildi 📝",
            message="Ustoz sizga 30 ta savollik yakuniy testni taqdim etdi. Testdan kamida 75% to'plasangiz kursni tamomlaysiz!",
            link="/videos/",
            icon="award"
        )
        return JsonResponse({
            'success': True,
            'message': f"{student.first_name or student.username} ga 30 ta savollik yakuniy test berildi."
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


def teacher_grade_homework_view(request):
    """
    Teacher / Admin tomonidan uy vazifasini tekshirish va baho qo'yish API (AJAX POST)
    """
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'error': 'Avval tizimga kiring!'}, status=401)

    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Faqat POST so\'rovi qabul qilinadi'}, status=405)

    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body.decode('utf-8'))
        else:
            data = request.POST

        homework_id = data.get('homework_id')
        score = data.get('score')
        feedback = data.get('feedback', '').strip()
        status = data.get('status', 'graded')

        if not homework_id:
            return JsonResponse({'success': False, 'error': 'Vazifa ID topilmadi'}, status=400)

        hw = get_object_or_404(HomeworkSubmission, id=homework_id)

        if score is not None and str(score).strip() != '':
            val = int(score)
            hw.score = max(1, min(10, val))
        hw.feedback = feedback
        hw.status = status
        hw.graded_by = request.user
        hw.graded_at = timezone.now()
        hw.save()

        # O'quvchiga bildirishnoma (Notification) yaratish
        sharh = hw.feedback or "A'lo natija!"
        Notification.objects.create(
            user=hw.user,
            title=f"Uy vazifangiz baholandi! ({hw.score}/10 ball) ⭐️",
            message=f"Ustoz {hw.direction} ({hw.lesson_id}-dars) bo'yicha vazifangizni baholadi. Sharh: {sharh}",
            link="/baholar/",
            icon="award"
        )

        # Telegram botga xabarnoma
        sharh_tg = hw.feedback or "A'lo darajada!"
        send_telegram_bot_message(
            f"⭐️ <b>Uy Vazifasi Baholandi!</b>\n\n"
            f"👤 <b>Talaba:</b> {hw.student_name} ({hw.group_name})\n"
            f"📚 <b>Kurs:</b> {hw.direction} (Dars #{hw.lesson_id})\n"
            f"🎯 <b>Baho:</b> <b>{hw.score}/10 ball</b>\n"
            f"💬 <b>Ustoz sharhi:</b> {sharh_tg}\n"
            f"👨‍🏫 <b>Baholagan ustoz:</b> {request.user.first_name or request.user.username}"
        )

        return JsonResponse({
            'success': True,
            'message': f"Vazifa muvaffaqiyatli baholandi! Qo'yilgan ball: {hw.score} ball.",
            'score': hw.score,
            'feedback': hw.feedback,
            'status': hw.status,
            'status_display': hw.get_status_display(),
            'graded_at': hw.graded_at.strftime('%d.%m.%Y %H:%M')
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


def certificate_view(request, cert_id):
    """
    1. Rasmiy QR-kodli Sertifikat sahifasi (PDF formatida chop etish imkoniyati bilan)
    """
    cert = get_object_or_404(Certificate, certificate_id=cert_id)
    verify_url = request.build_absolute_uri(f"/certificate/{cert.certificate_id}/")
    qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?size=180x180&data={urllib.parse.quote(verify_url)}"
    
    return render(request, 'courses/certificate.html', {
        'cert': cert,
        'verify_url': verify_url,
        'qr_code_url': qr_code_url,
    })


def get_notifications_api(request):
    """
    2. Jonli Bildirishnomalar ro'yxatini olish API
    """
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'unread_count': 0, 'notifications': []})

    notifs = Notification.objects.filter(user=request.user).order_by('-created_at')[:15]
    unread_count = Notification.objects.filter(user=request.user, is_read=False).count()

    data = []
    for n in notifs:
        data.append({
            'id': n.id,
            'title': n.title,
            'message': n.message,
            'link': n.link or '#',
            'icon': n.icon,
            'is_read': n.is_read,
            'created_at': n.created_at.strftime('%d.%m.%Y %H:%M')
        })

    return JsonResponse({'success': True, 'unread_count': unread_count, 'notifications': data})


def mark_notifications_read_api(request):
    """
    2. Bildirishnomalarni o'qilgan deb belgilash API
    """
    if not request.user.is_authenticated or request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Ruxsat berilmagan'}, status=400)

    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    return JsonResponse({'success': True, 'message': 'Barcha bildirishnomalar o\'qildi'})


def lesson_note_api(request):
    """
    3. Dars Konspekti (Shaxsiy Eslatmalar) API - O'qish va Avtomatik Saqlash
    """
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'error': 'Avval tizimga kiring'}, status=401)

    if request.method == 'GET':
        category_slug = request.GET.get('category_slug', 'web-dasturlash')
        lesson_id = int(request.GET.get('lesson_id', 1))
        note = LessonNote.objects.filter(user=request.user, category_slug=category_slug, lesson_id=lesson_id).first()
        return JsonResponse({'success': True, 'content': note.content if note else ''})

    elif request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                body = json.loads(request.body.decode('utf-8'))
            else:
                body = request.POST

            category_slug = body.get('category_slug', 'web-dasturlash')
            lesson_id = int(body.get('lesson_id', 1))
            content = body.get('content', '')

            note, _ = LessonNote.objects.get_or_create(
                user=request.user,
                category_slug=category_slug,
                lesson_id=lesson_id
            )
            note.content = content
            note.save()
            return JsonResponse({
                'success': True,
                'message': 'Konspekt saqlandi',
                'updated_at': note.updated_at.strftime('%H:%M:%S')
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Noto\'g\'ri so\'rov'}, status=405)


def ask_question_api(request):
    """
    4. Dars ostida "Ustozga Savol Berish" API
    """
    if not request.user.is_authenticated or request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Ruxsat berilmagan'}, status=400)

    try:
        if request.content_type == 'application/json':
            body = json.loads(request.body.decode('utf-8'))
        else:
            body = request.POST

        category_slug = body.get('category_slug', 'web-dasturlash')
        lesson_id = int(body.get('lesson_id', 1))
        question_text = body.get('question', '').strip()

        if not question_text:
            return JsonResponse({'success': False, 'error': 'Savol matnini kiriting!'}, status=400)

        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        student_name = request.user.get_full_name() or request.user.first_name or request.user.username
        group_name = profile.group_name or 'FN-24'

        q = LessonQuestion.objects.create(
            user=request.user,
            student_name=student_name,
            group_name=group_name,
            category_slug=category_slug,
            lesson_id=lesson_id,
            question=question_text
        )

        # Telegram botga xabarnoma yuborish
        send_telegram_bot_message(
            f"❓ <b>Yangi Savol (Dars Q&A)!</b>\n\n"
            f"👤 <b>Talaba:</b> {student_name} ({group_name})\n"
            f"📚 <b>Kurs:</b> {category_slug} (Dars #{lesson_id})\n"
            f"❓ <b>Savol:</b> {question_text}\n"
            f"🕐 <b>Vaqt:</b> {q.created_at.strftime('%d.%m.%Y %H:%M')}\n\n"
            f"👨‍🏫 <i>Teacher LMS orqali javob berishingiz mumkin</i>"
        )

        return JsonResponse({
            'success': True,
            'message': 'Savolingiz ustozga yuborildi! Tez orada javob olasiz.',
            'question_id': q.id,
            'student_name': student_name,
            'question': q.question,
            'created_at': q.created_at.strftime('%d.%m.%Y %H:%M')
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


def answer_question_api(request):
    """
    4. Ustoz tomonidan savolga javob yozish API
    """
    if not request.user.is_authenticated or request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Ruxsat berilmagan'}, status=400)

    try:
        if request.content_type == 'application/json':
            body = json.loads(request.body.decode('utf-8'))
        else:
            body = request.POST

        question_id = body.get('question_id')
        answer_text = body.get('answer', '').strip()

        if not question_id or not answer_text:
            return JsonResponse({'success': False, 'error': 'Javob matni bo\'sh'}, status=400)

        q = get_object_or_404(LessonQuestion, id=question_id)
        q.answer = answer_text
        q.answered_by = request.user
        q.answered_at = timezone.now()
        q.save()

        # O'quvchiga bildirishnoma (Notification) yaratish
        Notification.objects.create(
            user=q.user,
            title="Ustoz savolingizga javob berdi! 💬",
            message=f"Dars #{q.lesson_id} bo'yicha savolingizga javob: {answer_text[:120]}...",
            link=f"/videos/?category={q.category_slug}&video={q.lesson_id}",
            icon="message-circle"
        )

        # Telegram botga xabarnoma
        send_telegram_bot_message(
            f"💬 <b>Ustoz Savolga Javob Berdi!</b>\n\n"
            f"👤 <b>Talaba:</b> {q.student_name}\n"
            f"📚 <b>Kurs:</b> {q.category_slug} (Dars #{q.lesson_id})\n"
            f"❓ <b>Savol:</b> {q.question[:100]}\n"
            f"💡 <b>Ustoz javobi:</b> {answer_text}\n"
            f"👨‍🏫 <b>Ustoz:</b> {request.user.first_name or request.user.username}"
        )

        return JsonResponse({
            'success': True,
            'message': 'Javob saqlandi va talabaga yetkazildi!',
            'answer': q.answer,
            'answered_at': q.answered_at.strftime('%d.%m.%Y %H:%M')
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


def create_announcement_api(request):
    """
    5. Guruhlarga umumiy e'lon yuborish API
    """
    if not request.user.is_authenticated or request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Ruxsat berilmagan'}, status=400)

    try:
        if request.content_type == 'application/json':
            body = json.loads(request.body.decode('utf-8'))
        else:
            body = request.POST

        title = body.get('title', '').strip()
        content = body.get('content', '').strip()
        target_group = body.get('target_group', 'all').strip()

        if not title or not content:
            return JsonResponse({'success': False, 'error': 'Sarlavha va matn kiritilishi shart!'}, status=400)

        ann = Announcement.objects.create(
            author=request.user,
            title=title,
            content=content,
            target_group=target_group
        )

        # Mo'ljallangan talabalarga bildirishnoma yaratish
        target_users = User.objects.filter(is_superuser=False)
        if target_group != 'all':
            target_users = target_users.filter(profile__group_name=target_group)

        for u in target_users:
            Notification.objects.create(
                user=u,
                title=f"Yangi E'lon: {title} 📢",
                message=content[:150],
                link="/videos/",
                icon="bell"
            )

        # Telegram botga e'lon yuborish
        grp_text = "Barcha Guruhlar" if target_group == 'all' else f"Guruh: {target_group}"
        send_telegram_bot_message(
            f"📢 <b>Yangi Rasmiy E'lon!</b>\n\n"
            f"👥 <b>Kimga:</b> {grp_text}\n"
            f"📌 <b>Mavzu:</b> {title}\n\n"
            f"{content}\n\n"
            f"👨‍🏫 <b>Ustoz:</b> {request.user.first_name or request.user.username}"
        )

        return JsonResponse({
            'success': True,
            'message': 'E\'lon muvaffaqiyatli chop etildi!',
            'announcement_id': ann.id,
            'created_at': ann.created_at.strftime('%d.%m.%Y %H:%M')
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


def admin_platform_view(request):
    """
    Admin Platform Boshqaruv Markazi (Navy Blue & Sky Blue dizayn):
    1. Yangi ustozlarni qo'shish (username, email, password, ism)
    2. Har bir ustozda nechta student borligini ko'rish
    3. Barcha studentlarning login, password, email, created_at ma'lumotlari
    4. Barcha ustozlarning login, password, email ma'lumotlari
    """
    if not request.user.is_authenticated:
        return redirect('login')

    # Faqat superuser yoki admin roliga ega user kira oladi
    is_admin = request.user.is_superuser or (
        hasattr(request.user, 'profile') and request.user.profile.role == 'admin'
    )
    if not is_admin:
        messages.error(request, "Ushbu sahifaga faqat Bosh Administrator (Admin) kira oladi!")
        return redirect('portal')

    # Yangi Ustoz qo'shish (POST)
    if request.method == 'POST' and request.POST.get('action') == 'add_teacher':
        t_username = request.POST.get('username', '').strip()
        t_full_name = request.POST.get('full_name', '').strip()
        t_email = request.POST.get('email', '').strip()
        t_password = request.POST.get('password', '').strip()

        if not t_username or not t_password or not t_email:
            messages.error(request, "Login, parol va email kiritilishi shart!")
        elif User.objects.filter(username__iexact=t_username).exists():
            messages.error(request, f"'{t_username}' nomli foydalanuvchi allaqachon mavjud!")
        else:
            new_teacher = User.objects.create_user(
                username=t_username,
                email=t_email,
                password=t_password,
                first_name=t_full_name or t_username,
                is_staff=True,
                is_active=True
            )
            t_profile, _ = UserProfile.objects.get_or_create(user=new_teacher)
            t_profile.role = 'teacher'
            t_profile.is_approved = True
            t_profile.approval_status = 'approved'
            t_profile.plain_password = t_password
            t_profile.telegram_auth_code = t_password
            t_profile.save()

            messages.success(request, f"Yangi ustoz muvaffaqiyatli qo'shildi! Login: {t_username}, Parol: {t_password}")
            return redirect('admin_platform')

    # Barcha Ustozlar
    teachers_list = User.objects.filter(
        Q(is_superuser=True) | Q(profile__role='teacher') | Q(username='rixsi')
    ).distinct().select_related('profile').order_by('-date_joined')

    # Har bir ustozda nechta student borligini hisoblash
    teachers_data = []
    for t in teachers_list:
        tp = getattr(t, 'profile', None)
        pwd = (tp.plain_password if tp and tp.plain_password else (tp.telegram_auth_code if tp else '')) or ('123456' if t.username == 'rixsi' else 'Maxfiy/Shifrlangan')
        # Bu ustoz baholagan yoki qabul qilgan studentlar soni
        graded_students_count = HomeworkSubmission.objects.filter(graded_by=t).values('user').distinct().count()
        # Agar rixsi bo'lsa barcha tasdiqlangan studentlar
        if t.username == 'rixsi' or t.is_superuser:
            student_count = User.objects.filter(is_superuser=False, profile__is_approved=True).count()
        else:
            student_count = graded_students_count

        teachers_data.append({
            'user': t,
            'full_name': t.get_full_name() or t.first_name or t.username,
            'username': t.username,
            'email': t.email or "Kiritilmagan",
            'password': pwd,
            'created_at': t.date_joined,
            'student_count': student_count,
            'is_superuser': t.is_superuser,
        })

    # Barcha Talabalar
    students_list = User.objects.filter(is_superuser=False).select_related('profile').order_by('-date_joined')
    students_data = []
    for s in students_list:
        sp = getattr(s, 'profile', None)
        pwd = (sp.plain_password if sp and sp.plain_password else (sp.telegram_auth_code if sp else '')) or '123456'
        
        # O'zlashtirish foizi: Yo'nalishdagi 10 ta darsdan nechtasi topshirilgan / baholangan
        total_lessons = 10
        graded_count = HomeworkSubmission.objects.filter(user=s, status='graded').count()
        submitted_count = HomeworkSubmission.objects.filter(user=s).count()
        progress_pct = min(100, round((graded_count / total_lessons) * 100)) if total_lessons else 0

        students_data.append({
            'user': s,
            'full_name': s.get_full_name() or s.first_name or s.username,
            'username': s.username,
            'email': s.email or "Kiritilmagan",
            'password': pwd,
            'created_at': s.date_joined,
            'direction': sp.direction if sp else "Belgilanmagan",
            'group_name': sp.group_name if sp else "Guruhsiz",
            'is_approved': sp.is_approved if sp else False,
            'approval_status': sp.get_approval_status_display() if sp else "Noma'lum",
            'progress_pct': progress_pct,
            'submitted_count': submitted_count,
            'graded_count': graded_count,
        })

    # Statistika
    total_teachers = len(teachers_data)
    total_students = len(students_data)
    total_approved_students = sum(1 for s in students_data if s['is_approved'])
    total_certificates = Certificate.objects.count()

    context = {
        'teachers_data': teachers_data,
        'students_data': students_data,
        'total_teachers': total_teachers,
        'total_students': total_students,
        'total_approved_students': total_approved_students,
        'total_certificates': total_certificates,
    }
    return render(request, 'dashboard/admin_platform.html', context)


# ============================================================================
# TALABA BATAFSIL MA'LUMOTLARI API (TEACHER MODAL UCHUN)
# ============================================================================

def api_teacher_student_detail(request, student_id):
    """
    Teacher platformada talaba ustiga bosilganda uning dars o'zlashtirish foizi
    va barcha topshirgan vazifalari, baholari bilan batafsil modal ma'lumotlarini qaytaradi.
    """
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'error': 'Avtorizatsiyadan o\'tilmagan'}, status=401)

    student = get_object_or_404(User, id=student_id)
    profile, _ = UserProfile.objects.get_or_create(user=student)

    # Homeworklar
    submissions = HomeworkSubmission.objects.filter(user=student).order_by('-submitted_at')
    hw_list = []
    total_score = 0
    graded_count = 0
    for h in submissions:
        if h.score is not None:
            total_score += h.score
            graded_count += 1
        hw_list.append({
            'id': h.id,
            'lesson_id': h.lesson_id,
            'direction': h.direction,
            'category_slug': h.category_slug,
            'status': h.status,
            'status_display': h.get_status_display(),
            'score': h.score,
            'feedback': h.feedback,
            'text_content': h.text_content,
            'github_link': h.github_link,
            'submitted_at': h.submitted_at.strftime('%d.%m.%Y %H:%M'),
            'graded_at': h.graded_at.strftime('%d.%m.%Y %H:%M') if h.graded_at else None,
        })

    # O'zlashtirish foizi (10 ta asosiy dars bo'yicha)
    total_lessons = 10
    progress_percentage = min(100, round((graded_count / total_lessons) * 100))
    avg_score = round(total_score / graded_count, 1) if graded_count > 0 else 0
    submitted_lessons_set = set(HomeworkSubmission.objects.filter(user=student).values_list('lesson_id', flat=True))
    required_lessons_set = set(range(1, 11))
    all_lessons_completed = required_lessons_set.issubset(submitted_lessons_set)
    can_take_test, c_hours, c_mins = profile.can_take_final_test()

    # Ruxsat berilgan darslar
    unlocks = list(UserVideoUnlock.objects.filter(user=student).values('category_slug', 'lesson_id'))

    # Sertifikat
    cert = Certificate.objects.filter(user=student).first()

    return JsonResponse({
        'success': True,
        'student': {
            'id': student.id,
            'username': student.username,
            'full_name': student.get_full_name() or student.first_name or student.username,
            'email': student.email,
            'group_name': profile.group_name,
            'direction': profile.direction,
            'direction_slug': profile.get_direction_slug(),
            'created_at': student.date_joined.strftime('%d.%m.%Y %H:%M'),
            'is_approved': profile.is_approved,
            'approval_status': profile.get_approval_status_display(),
            'progress_percentage': progress_percentage,
            'total_lessons': total_lessons,
            'graded_lessons': graded_count,
            'avg_score': avg_score,
            'is_final_test_granted': profile.is_final_test_granted(),
            'has_certificate': bool(cert),
            'certificate_id': cert.certificate_id if cert else None,
            'all_lessons_completed': all_lessons_completed,
            'submitted_lessons_count': len(submitted_lessons_set.intersection(required_lessons_set)),
            'missing_lessons': [l for l in sorted(required_lessons_set - submitted_lessons_set)],
            'can_take_final_test': can_take_test,
            'cooldown_hours': c_hours,
            'cooldown_minutes': c_mins,
            'final_test_score': profile.final_test_score,
        },
        'homeworks': hw_list,
        'unlocks': unlocks,
    })


# ============================================================================
# TALABA YO'NALISH O'ZGARTIRISH SO'ROVI VA USTOZ TASDIQLASHI
# ============================================================================

def request_direction_change_api(request):
    """
    Talaba kursni tugatib sertifikat olgandan so'ng yangi yo'nalishni tanlaydi.
    Ustozga taklifnoma (priglasheniya) yuboriladi va Telegram botga xabar ketadi.
    """
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'error': 'Avval tizimga kiring'}, status=401)

    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Faqat POST so\'rovi qabul qilinadi'}, status=405)

    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body.decode('utf-8'))
        else:
            data = request.POST

        requested_slug = data.get('direction_slug', '').strip()
        direction_names = {
            'python-backend': 'Python Backend',
            'web-dasturlash': 'Web Dasturlash',
            'ai-data-science': "Sun'iy Intellekt & Data Science",
            'mobile-dev': 'Mobil Dasturlash (Flutter)',
            'ui-ux-design': 'UI/UX Dizayn',
            'kiberxavfsizlik': 'Kiberxavfsizlik',
        }

        requested_name = direction_names.get(requested_slug)
        if not requested_name:
            return JsonResponse({'success': False, 'error': 'Noto\'g\'ri yo\'nalish tanlandi!'}, status=400)

        profile, _ = UserProfile.objects.get_or_create(user=request.user)

        # Allaqachon tugatilgan yo'nalishmi?
        if requested_slug in profile.get_completed_directions_list():
            return JsonResponse({'success': False, 'error': 'Ushbu yo\'nalishni allaqachon tamomlagansiz!'}, status=400)

        # Yangi so'rov yaratish yoki mavjud kutilayotgan so'rovni yangilash
        req_obj, created = DirectionChangeRequest.objects.get_or_create(
            user=request.user,
            requested_direction_slug=requested_slug,
            defaults={
                'requested_direction': requested_name,
                'status': 'pending'
            }
        )
        if not created and req_obj.status != 'pending':
            req_obj.status = 'pending'
            req_obj.save()

        student_name = request.user.get_full_name() or request.user.first_name or request.user.username

        # Teacher va superadminlarga tizim bildirishnomasi (Notification) yuborish
        try:
            teachers = User.objects.filter(Q(is_superuser=True) | Q(profile__role='teacher') | Q(username='rixsi')).distinct()
            for teacher in teachers:
                Notification.objects.create(
                    user=teacher,
                    title=f"🚀 Yangi yo'nalish taklifnomasi: {student_name}",
                    message=f"{student_name} ({profile.group_name}) '{profile.direction}' kursini tugatib, yangi '{requested_name}' yo'nalishiga o'tish so'rovini yubordi.",
                    link="/teacher/?tab=direction_requests",
                    icon="graduation-cap"
                )
        except Exception:
            pass

        # Telegram bot orqali Ustozga xabarnoma (Priglasheniya)
        send_telegram_bot_message(
            f"🚀 <b>Yangi Yo'nalish So'rovi (Taklifnoma)!</b>\n\n"
            f"👤 <b>Talaba:</b> {student_name} ({profile.group_name})\n"
            f"🎓 <b>Eski yo'nalishi:</b> {profile.direction} (Tamomlangan)\n"
            f"🎯 <b>Tanlangan yangi yo'nalish:</b> <b>{requested_name}</b>\n"
            f"🕐 <b>Vaqt:</b> {timezone.now().strftime('%d.%m.%Y %H:%M')}\n\n"
            f"👨‍🏫 <i>Ustoz, Teacher LMS da ushbu taklifnomani qabul qiling!</i>"
        )

        return JsonResponse({
            'success': True,
            'message': f"'{requested_name}' yo'nalishi bo'yicha taklifnomangiz ustozga yuborildi! Ustoz qabul qilgandan so'ng darslar ochiladi.",
            'requested_direction': requested_name,
            'status': 'pending'
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


def teacher_approve_direction_change_api(request):
    """
    Ustoz yangi yo'nalishga o'tish so'rovini (priglasheniya) qabul qiladi yoki rad etadi.
    Qabul qilinganda talabaning profili yangilanadi va yangi yo'nalish videolari ochiladi.
    """
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'error': 'Avtorizatsiyadan o\'tilmagan'}, status=401)

    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.user.username != 'rixsi' and not request.user.is_superuser and profile.role != 'teacher':
        return JsonResponse({'success': False, 'error': 'Ruxsat etilmagan'}, status=403)

    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Faqat POST so\'rovi qabul qilinadi'}, status=405)

    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body.decode('utf-8'))
        else:
            data = request.POST

        request_id = data.get('request_id')
        action = data.get('action', 'approve') # 'approve' yoki 'reject'

        req_obj = get_object_or_404(DirectionChangeRequest, id=request_id)
        student_user = req_obj.user
        student_profile, _ = UserProfile.objects.get_or_create(user=student_user)

        if action == 'approve':
            req_obj.status = 'approved'
            req_obj.teacher = request.user
            req_obj.save()

            # Talabaning yangi yo'nalishini saqlaymiz
            student_profile.direction = req_obj.requested_direction
            student_profile.is_approved = True
            student_profile.approval_status = 'approved'
            student_profile.save(update_fields=['direction', 'is_approved', 'approval_status'])

            # 1-darsni avtomatik ochib beramiz
            UserVideoUnlock.objects.get_or_create(
                user=student_user,
                category_slug=req_obj.requested_direction_slug,
                lesson_id=1,
                defaults={'unlocked_by': request.user}
            )

            # Talabaga bildirishnoma
            Notification.objects.create(
                user=student_user,
                title=f"Yangi yo'nalish tasdiqlandi! 🎉",
                message=f"Ustozingiz '{req_obj.requested_direction}' yo'nalishingizni qabul qildi. Video darslarni boshlashingiz mumkin!",
                link="/videos/",
                icon="circle-check"
            )

            # Telegram bot xabari
            send_telegram_bot_message(
                f"✅ <b>Yo'nalish So'rovi Qabul Qilindi!</b>\n\n"
                f"👤 <b>Talaba:</b> {student_user.get_full_name() or student_user.username}\n"
                f"🎯 <b>Yangi yo'nalish:</b> {req_obj.requested_direction}\n"
                f"👨‍🏫 <b>Tasdiqlagan ustoz:</b> {request.user.first_name or request.user.username}\n"
                f"🚀 <i>1-dars avtomatik ochildi!</i>"
            )

            return JsonResponse({
                'success': True,
                'message': f"Talaba {student_user.username} yangi '{req_obj.requested_direction}' yo'nalishiga muvaffaqiyatli qabul qilindi!",
                'status': 'approved'
            })
        else:
            req_obj.status = 'rejected'
            req_obj.teacher = request.user
            req_obj.save()

            Notification.objects.create(
                user=student_user,
                title="Yo'nalish so'rovi rad etildi",
                message=f"'{req_obj.requested_direction}' yo'nalishi bo'yicha so'rovingiz ustoz tomonidan rad etildi.",
                link="/learnify/",
                icon="x-circle"
            )

            return JsonResponse({
                'success': True,
                'message': f"So'rov rad etildi.",
                'status': 'rejected'
            })

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


def check_direction_status_api(request):
    """
    Talabaning yangi yo'nalish so'rovi holatini tekshirish (Real-time polling)
    Ustoz tasdiqlagach, sahifa avtomatik yangilanib faqat yangi yo'nalish darslari ochiladi.
    """
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'error': "Avtorizatsiyadan o'tilmagan"}, status=401)

    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    
    pending_req = DirectionChangeRequest.objects.filter(user=request.user, status='pending').first()
    if pending_req:
        return JsonResponse({
            'success': True,
            'status': 'pending',
            'requested_direction': pending_req.requested_direction,
            'requested_slug': pending_req.requested_direction_slug
        })

    # Agar oxirgi so'rov tasdiqlangan bo'lsa
    approved_req = DirectionChangeRequest.objects.filter(user=request.user, status='approved').order_by('-updated_at').first()
    if approved_req and profile.direction == approved_req.requested_direction:
        return JsonResponse({
            'success': True,
            'status': 'approved',
            'current_direction': profile.direction,
            'direction_slug': profile.get_direction_slug(),
            'message': f"Ustoz yangi '{profile.direction}' yo'nalishingizni tasdiqladi!"
        })

    return JsonResponse({
        'success': True,
        'status': 'idle',
        'current_direction': profile.direction,
        'direction_slug': profile.get_direction_slug()
    })


# ============================================================================
# 30 TA SAVOLDAN IBORAT YAKUNIY TEST API (75% O'TISH BALI VA 2 KUN COOLDOWN)
# ============================================================================

def get_final_test_questions_api(request):
    """
    O'quvchiga 30 ta savoldan iborat yakuniy test savollarini beradi.
    Faqat ustoz ruxsat bergan va 2 kunlik cooldown tugagan bo'lsa ochiladi.
    """
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'error': "Avval tizimga kiring!"}, status=401)

    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    slug = profile.get_direction_slug()

    if not profile.is_final_test_granted(slug):
        return JsonResponse({
            'success': False,
            'error': "Ustoz hali sizga yakuniy testni bermagan! Avval barcha darslarni tugating va ustozingiz test berishini kuting."
        }, status=403)

    can_take, hours, minutes = profile.can_take_final_test()
    if not can_take:
        return JsonResponse({
            'success': False,
            'cooldown': True,
            'hours_left': hours,
            'minutes_left': minutes,
            'error': f"Siz yakuniy testdan o'ta olmagansiz. Qayta test topshirish faqat 2 kundan keyin mumkin! Qolgan vaqt: {hours} soat {minutes} daqiqa."
        }, status=403)

    from Courses.final_test_data import get_final_test_for_slug
    raw_questions = get_final_test_for_slug(slug)
    client_questions = []
    for q in raw_questions:
        client_questions.append({
            'id': q['id'],
            'question': q['question'],
            'options': q['options']
        })

    return JsonResponse({
        'success': True,
        'direction': profile.direction,
        'slug': slug,
        'questions': client_questions,
        'total': len(client_questions),
        'passing_percentage': 75
    })


def submit_final_test_api(request):
    """
    O'quvchining 30 ta savoldan iborat yakuniy test javoblarini tekshiradi:
    - O'tish foizi: 75% (30 tadan kamida 23 ta to'g'ri)
    - Agar >= 75%:
      "Tabriklaymiz, siz kursdan o'tdingiz!"
      Kurs yakunlanadi, sertifikat beriladi, yangi yo'nalish tanlash overlayi ochiladi.
    - Agar < 75%:
      Keyingi test faqat 2 kundan keyin topshirilishi mumkin.
    """
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'error': "Avval tizimga kiring!"}, status=401)

    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': "Faqat POST so'rovi qabul qilinadi"}, status=405)

    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    slug = profile.get_direction_slug()

    if not profile.is_final_test_granted(slug):
        return JsonResponse({
            'success': False,
            'error': "Ustoz hali sizga yakuniy testni taqdim etmagan!"
        }, status=403)

    can_take, hours, minutes = profile.can_take_final_test()
    if not can_take:
        return JsonResponse({
            'success': False,
            'cooldown': True,
            'error': f"Keyingi test faqat 2 kundan keyin topshirilishi mumkin! Qolgan vaqt: {hours} soat {minutes} daqiqa."
        }, status=403)

    try:
        data = json.loads(request.body.decode('utf-8'))
        answers = data.get('answers', {})
    except Exception as e:
        return JsonResponse({'success': False, 'error': "Noto'g'ri ma'lumot formati"}, status=400)

    from Courses.final_test_data import get_final_test_for_slug
    raw_questions = get_final_test_for_slug(slug)
    total = len(raw_questions)
    correct_count = 0

    for q in raw_questions:
        qid_str = str(q['id'])
        user_choice = answers.get(qid_str)
        if user_choice is None:
            user_choice = answers.get(q['id'])
        if user_choice is not None and int(user_choice) == q['correct']:
            correct_count += 1

    score_pct = round((correct_count / total) * 100) if total > 0 else 0
    passed = (score_pct >= 75)

    now = timezone.now()
    profile.final_test_score = score_pct
    profile.final_test_last_attempt = now

    if passed:
        profile.complete_current_direction()
        profile.save()

        # Sertifikat yaratish
        student_full_name = request.user.get_full_name() or request.user.first_name or request.user.username
        cert_id = f"LRN-{now.strftime('%Y%m')}-{uuid.uuid4().hex[:6].upper()}"
        cert, created = Certificate.objects.get_or_create(
            user=request.user,
            direction_slug=slug,
            defaults={
                'certificate_id': cert_id,
                'full_name': student_full_name,
                'direction': profile.direction,
                'avg_score': round(score_pct / 10.0, 1),
            }
        )

        Notification.objects.create(
            user=request.user,
            title="Tabriklaymiz! Siz kursdan o'tdingiz 🎓",
            message=f"Siz yakuniy testdan {score_pct}% to'plab ({correct_count}/{total}), '{profile.direction}' kursini muvaffaqiyatli tamomladingiz!",
            link=f"/certificate/{cert.certificate_id}/",
            icon="award"
        )

        send_telegram_bot_message(
            f"🎓 <b>Kurs Muvaffaqiyatli Tamomlandi!</b>\n\n"
            f"👤 <b>Talaba:</b> {cert.full_name}\n"
            f"🏆 <b>Kurs:</b> {cert.direction}\n"
            f"📊 <b>Yakuniy test natijasi:</b> {score_pct}% ({correct_count}/30 to'g'ri)\n"
            f"🏅 <b>Sertifikat ID:</b> <code>{cert.certificate_id}</code>\n\n"
            f"🌐 <i>Learnify Ta'lim Platformasi</i>"
        )

        return JsonResponse({
            'success': True,
            'passed': True,
            'score': score_pct,
            'correct_count': correct_count,
            'total': total,
            'message': "Tabriklaymiz! Siz kursdan o'tdingiz!",
            'certificate_id': cert.certificate_id
        })
    else:
        profile.save()
        Notification.objects.create(
            user=request.user,
            title="Yakuniy test natijasi ⚠️",
            message=f"Siz testdan {score_pct}% to'pladingiz ({correct_count}/{total}). O'tish bali 75%. Keyingi test faqat 2 kundan keyin topshirilishi mumkin.",
            link="/videos/",
            icon="clock"
        )
        return JsonResponse({
            'success': True,
            'passed': False,
            'score': score_pct,
            'correct_count': correct_count,
            'total': total,
            'message': f"Afsuski, siz {score_pct}% to'pladingiz ({correct_count}/{total}). O'tish bali 75%. Keyingi test faqat 2 kundan keyin topshirilishi mumkin."
        })
