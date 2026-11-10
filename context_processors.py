from datetime import timedelta
from django.utils import timezone
from django.db.models import Q
from .models import UserProfile, HomeworkSubmission, Notification, Announcement


def user_stats(request):
    """
    Real vaqt rejimida har bir foydalanuvchining:
    - Ketma-ket tashrif kunlari (Real Streak - hech qanday soxta 7 kunlarsiz)
    - Olingan ustoz baholari soni (Grades Count)
    - O'qilmagan bildirishnomalar soni va oxirgi bildirishnomalar
    - Guruh e'lonlari
    ni barcha sahifalarga uzatadi.
    """
    if not request.user.is_authenticated:
        return {
            'user_streak': 0,
            'user_grades_count': 0,
            'unread_notifs_count': 0,
            'recent_notifications': [],
            'latest_announcement': None,
        }

    streak = 1
    user_direction = "Web Dasturlash"
    user_direction_slug = "web-dasturlash"
    is_direction_completed = False
    completed_directions_list = []
    unread_notifs_count = 0
    recent_notifications = []
    latest_announcement = None

    try:
        profile, created = UserProfile.objects.get_or_create(
            user=request.user,
            defaults={
                'role': 'student',
                'group_name': 'FN-24',
                'direction': 'Web Dasturlash',
                'current_streak': 1,
                'last_visit_date': timezone.localdate(),
            }
        )

        user_direction = profile.direction
        user_direction_slug = profile.get_direction_slug()
        is_direction_completed = profile.is_current_direction_completed()
        completed_directions_list = profile.get_completed_directions_list()

        today = timezone.localdate()
        if profile.last_visit_date is None:
            profile.current_streak = 1
            profile.last_visit_date = today
            profile.save(update_fields=['current_streak', 'last_visit_date'])
        elif profile.last_visit_date == today:
            # Bugun allaqachon kirgan, streak saqlanadi
            pass
        elif profile.last_visit_date == today - timedelta(days=1):
            # Kecha kirgan, ketma-ketlik +1 bo'ladi
            profile.current_streak += 1
            profile.last_visit_date = today
            profile.save(update_fields=['current_streak', 'last_visit_date'])
        else:
            # Orada kun qoldirilgan bo'lsa streak 1 dan boshlanadi
            profile.current_streak = 1
            profile.last_visit_date = today
            profile.save(update_fields=['current_streak', 'last_visit_date'])

        streak = profile.current_streak
        
        # Bildirishnomalar va e'lonlar
        unread_notifs_count = Notification.objects.filter(user=request.user, is_read=False).count()
        recent_notifications = list(Notification.objects.filter(user=request.user)[:7])
        group = getattr(profile, 'group_name', 'FN-24')
        latest_announcement = Announcement.objects.filter(
            Q(target_group='all') | Q(target_group=group)
        ).order_by('-created_at').first()

        # Kutilayotgan yo'nalish so'rovi (priglasheniya)
        from .models import DirectionChangeRequest
        pending_direction_request = DirectionChangeRequest.objects.filter(user=request.user, status='pending').first()

        all_direction_options = [
            {'slug': 'python-backend', 'name': 'Python Backend', 'icon': 'fa-brands fa-python', 'color': '#a855f7', 'desc': "Django, PostgreSQL, REST API va Server arxitekturasi"},
            {'slug': 'web-dasturlash', 'name': 'Web Dasturlash', 'icon': 'fa-solid fa-code', 'color': '#38bdf8', 'desc': "HTML5, CSS3, JavaScript, React.js zamonaviy Frontend va Fullstack"},
            {'slug': 'ai-data-science', 'name': "Sun'iy Intellekt & Data Science", 'icon': 'fa-solid fa-brain', 'color': '#ec4899', 'desc': "Machine Learning, Deep Learning, Neyron tarmoqlar va Big Data"},
            {'slug': 'mobile-dev', 'name': 'Mobil Dasturlash (Flutter)', 'icon': 'fa-solid fa-mobile-screen', 'color': '#10b981', 'desc': "Flutter, Dart, iOS va Android mobil ilovalar yaratish"},
            {'slug': 'ui-ux-design', 'name': 'UI/UX Dizayn', 'icon': 'fa-solid fa-palette', 'color': '#f59e0b', 'desc': "Figma, Prototyping, Wireframing va zamonaviy interfeys dizaynlari"},
            {'slug': 'kiberxavfsizlik', 'name': 'Kiberxavfsizlik', 'icon': 'fa-solid fa-shield-halved', 'color': '#ef4444', 'desc': "Axborot xavfsizligi, Tarmoq himoyasi, Etik xakerlik va Pentesting"},
        ]
        available_next_directions = [d for d in all_direction_options if d['slug'] not in completed_directions_list]

    except Exception:
        streak = 1

    try:
        grades_count = HomeworkSubmission.objects.filter(
            user=request.user,
            status='graded'
        ).count()
    except Exception:
        grades_count = 0

    return {
        'user_streak': streak,
        'user_grades_count': grades_count,
        'user_direction': user_direction,
        'user_direction_slug': user_direction_slug,
        'is_direction_completed': is_direction_completed,
        'completed_directions_list': completed_directions_list,
        'unread_notifs_count': unread_notifs_count,
        'recent_notifications': recent_notifications,
        'latest_announcement': latest_announcement,
        'pending_direction_request': pending_direction_request,
        'available_next_directions': available_next_directions,
    }
