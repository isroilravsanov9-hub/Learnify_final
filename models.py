from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    icon = models.CharField(max_length=50, default="code", verbose_name="Ikonka (masalan: code, palette, database)")

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL_CHOICES = [
        ('beginner', "Boshlang'ich"),
        ('intermediate', "O'rta"),
        ('advanced', "Murakkab"),
    ]

    title = models.CharField(max_length=200, verbose_name="Kurs nomi")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses", verbose_name="Kategoriya")
    short_description = models.CharField(max_length=300, verbose_name="Qisqa tavsif")
    description = models.TextField(verbose_name="Batafsil ma'lumot")
    instructor_name = models.CharField(max_length=150, verbose_name="O'qituvchi ismi")
    instructor_role = models.CharField(max_length=150, default="Senior Dasturchi", verbose_name="O'qituvchi mutaxassisligi")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Narxi (so'm)")
    discount_price = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True, verbose_name="Chegirma narxi (so'm)")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner', verbose_name="Daraja")
    duration_hours = models.PositiveIntegerField(default=24, verbose_name="Davomiyligi (soat)")
    lessons_count = models.PositiveIntegerField(default=35, verbose_name="Darslar soni")
    students_count = models.PositiveIntegerField(default=120, verbose_name="O'quvchilar soni")
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.9, verbose_name="Reyting")
    rating_count = models.PositiveIntegerField(default=48, verbose_name="Baho berganlar soni")
    badge = models.CharField(max_length=50, blank=True, default="Ommabop", verbose_name="Belgi (Badge)")
    youtube_id = models.CharField(max_length=50, default="HGTJBPNC-Gw", verbose_name="YouTube Video ID")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class TypingScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="typing_scores")
    player_name = models.CharField(max_length=100, verbose_name="O'yinchi ismi")
    wpm = models.PositiveIntegerField(verbose_name="WPM (Tezlik)")
    accuracy = models.PositiveIntegerField(verbose_name="Aniqlik (%)")
    mode = models.CharField(max_length=50, default="code", verbose_name="Rejim")
    time_limit = models.PositiveIntegerField(default=30, verbose_name="Vaqt (soniya)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Sana")

    class Meta:
        verbose_name = "Typing Natijasi"
        verbose_name_plural = "Typing Natijalari (Leaderboard)"
        ordering = ['-wpm', '-accuracy', '-created_at']

    def __str__(self):
        return f"{self.player_name}: {self.wpm} WPM ({self.accuracy}%)"


class UserVideoUnlock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="video_unlocks", verbose_name="Foydalanuvchi")
    category_slug = models.CharField(max_length=50, default="all", verbose_name="Kategoriya (yoki 'all')")
    lesson_id = models.IntegerField(default=0, verbose_name="Dars ID (0 = barcha darslar)")
    unlocked_for_all_users = models.BooleanField(default=False, verbose_name="Hamma uchun ochiqmi?")
    unlocked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="granted_unlocks", verbose_name="Ochib bergan admin")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Video Ruxsati (Qulfdan chiqarish)"
        verbose_name_plural = "Video Ruxsatlari (Qulfdan chiqarishlar)"

    def __str__(self):
        target = "Hamma foydalanuvchilar" if self.unlocked_for_all_users else (self.user.username if self.user else "Anonim")
        return f"{target} -> {self.category_slug} (Dars #{self.lesson_id or 'Barchasi'})"


class HomeworkSubmission(models.Model):
    STATUS_CHOICES = (
        ('submitted', "Yangi (Topshirildi)"),
        ('in_review', "Ko'rib chiqilmoqda"),
        ('graded', "Baholandi"),
        ('rejected', "Qayta ishlashga qaytarildi"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="homework_submissions", verbose_name="Foydalanuvchi")
    category_slug = models.CharField(max_length=50, verbose_name="Kurs Yo'nalishi")
    lesson_id = models.IntegerField(default=1, verbose_name="Dars Raqami")
    student_name = models.CharField(max_length=150, blank=True, verbose_name="O'quvchi Ismi")
    group_name = models.CharField(max_length=50, blank=True, default="FN-24", verbose_name="Guruhi")
    direction = models.CharField(max_length=100, blank=True, default="Python Backend", verbose_name="Yo'nalishi")
    text_content = models.TextField(blank=True, verbose_name="Yechim / Matn / Izoh")
    file = models.FileField(upload_to='homework_files/', blank=True, null=True, verbose_name="Yuklangan Fayl")
    github_link = models.CharField(max_length=500, blank=True, verbose_name="GitHub yoki Live Demo Havola")
    
    # O'qituvchi baholash qismi
    score = models.IntegerField(null=True, blank=True, verbose_name="Qo'yilgan Baho (1-10 ball)")
    feedback = models.TextField(blank=True, verbose_name="O'qituvchi Bahosi / Sharhi")
    graded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="graded_homeworks", verbose_name="Baholagan O'qituvchi")
    graded_at = models.DateTimeField(null=True, blank=True, verbose_name="Baholangan Vaqt")
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted', verbose_name="Holat")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Topshirilgan Vaqt")

    class Meta:
        verbose_name = "Uy Vazifasi Topshirig'i"
        verbose_name_plural = "Uy Vazifalari (Topshiriqlar)"
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.student_name or self.user.username} [{self.group_name}] - {self.direction} (Dars #{self.lesson_id}) - {self.get_status_display()}"


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('student', "O'quvchi (Talaba)"),
        ('teacher', "O'qituvchi (Mentor)"),
        ('admin', "Bosh Administrator"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student', verbose_name="Roli")
    group_name = models.CharField(max_length=50, default="FN-24", verbose_name="Guruhi")
    direction = models.CharField(max_length=100, default="Python Backend", verbose_name="Yo'nalishi")
    phone = models.CharField(max_length=30, blank=True, verbose_name="Telefon")
    bio = models.TextField(blank=True, verbose_name="Qisqa Ma'lumot")
    current_streak = models.PositiveIntegerField(default=1, verbose_name="Ketma-ket kirgan kunlar (Streak)")
    last_visit_date = models.DateField(null=True, blank=True, verbose_name="Oxirgi tashrif sanasi")
    completed_directions = models.CharField(max_length=500, blank=True, default="", verbose_name="Tugatilgan yo'nalishlar")
    final_test_granted = models.CharField(max_length=500, blank=True, default="", verbose_name="Yakuniy test berilgan yo'nalishlar")
    
    # Ro'yxatdan o'tish va O'qituvchi tasdiqlashi (Teacher Approval)
    is_approved = models.BooleanField(default=True, verbose_name="O'qituvchi tomonidan tasdiqlanganmi?")
    approval_status = models.CharField(max_length=20, default='approved', choices=[
        ('pending_telegram', "Telegram kod kutilmoqda"),
        ('pending_teacher', "O'qituvchi qabul qilishi kutilmoqda"),
        ('approved', "Qabul qilindi (Tasdiqlangan)"),
        ('rejected', "Rad etildi"),
    ], verbose_name="A'zolik holati")
    telegram_chat_id = models.CharField(max_length=50, blank=True, null=True, verbose_name="Telegram Chat ID")
    telegram_username = models.CharField(max_length=100, blank=True, null=True, verbose_name="Telegram Username (@username)")
    telegram_auth_code = models.CharField(max_length=50, blank=True, null=True, verbose_name="Telegram bir martalik parol/kod")
    telegram_code_verified = models.BooleanField(default=False, verbose_name="Telegram paroli tasdiqlanganmi?")
    plain_password = models.CharField(max_length=128, blank=True, default="", verbose_name="Dastlabki/Joriy Parol (Admin uchun)")
    final_test_last_attempt = models.DateTimeField(null=True, blank=True, verbose_name="Oxirgi yakuniy test urinishi vaqti")
    final_test_score = models.IntegerField(null=True, blank=True, verbose_name="Oxirgi yakuniy test natijasi (%)")
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Foydalanuvchi Profili"
        verbose_name_plural = "Foydalanuvchi Profillari"

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()}) - Guruh: {self.group_name}"

    def get_completed_directions_list(self):
        if not self.completed_directions:
            return []
        return [d.strip() for d in self.completed_directions.split(',') if d.strip()]

    def get_direction_slug(self):
        dt = (self.direction or '').lower()
        if 'web' in dt or 'veb' in dt or 'frontend' in dt:
            return 'web-dasturlash'
        elif 'python' in dt or 'django' in dt or 'backend' in dt:
            return 'python-backend'
        elif 'ai' in dt or 'sun' in dt or 'data' in dt:
            return 'ai-data-science'
        elif 'mobil' in dt or 'flutter' in dt or 'dart' in dt:
            return 'mobile-dev'
        elif 'ui' in dt or 'ux' in dt or 'design' in dt or 'dizayn' in dt:
            return 'ui-ux-design'
        elif 'kiber' in dt or 'cyber' in dt or 'xavfsiz' in dt:
            return 'kiberxavfsizlik'
        return 'web-dasturlash'

    def is_current_direction_completed(self):
        slug = self.get_direction_slug()
        return slug in self.get_completed_directions_list()

    def is_final_test_granted(self, slug=None):
        slug = slug or self.get_direction_slug()
        return slug in [d.strip() for d in self.final_test_granted.split(',') if d.strip()]

    def grant_final_test(self, slug):
        granted = [d.strip() for d in self.final_test_granted.split(',') if d.strip()]
        if slug not in granted:
            granted.append(slug)
            self.final_test_granted = ",".join(granted)
            self.save(update_fields=['final_test_granted'])

    def can_take_final_test(self):
        """
        Agar o'quvchi oxirgi testdan 75% dan kam olgan bo'lsa, 2 kun kutishi shart.
        Qaytaradi: (mumkinmi: bool, qolgan_soat: int, qolgan_daqiqa: int)
        """
        if not self.final_test_last_attempt:
            return True, 0, 0
        from django.utils import timezone
        from datetime import timedelta
        cooldown_end = self.final_test_last_attempt + timedelta(days=2)
        now = timezone.now()
        if now < cooldown_end:
            diff = cooldown_end - now
            total_seconds = int(diff.total_seconds())
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            return False, hours, minutes
        return True, 0, 0

    def complete_current_direction(self):
        slug = self.get_direction_slug()
        c_list = self.get_completed_directions_list()
        if slug not in c_list:
            c_list.append(slug)
            self.completed_directions = ",".join(c_list)
            self.save(update_fields=['completed_directions'])
        return True


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    message = models.TextField(verbose_name="Xabar")
    link = models.CharField(max_length=255, blank=True, default="", verbose_name="Havola")
    icon = models.CharField(max_length=50, default="bell", verbose_name="Ikonka")
    is_read = models.BooleanField(default=False, verbose_name="O'qilganmi?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vaqt")

    class Meta:
        verbose_name = "Bildirishnoma"
        verbose_name_plural = "Bildirishnomalar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}: {self.title}"


class LessonNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lesson_notes")
    category_slug = models.CharField(max_length=50, verbose_name="Kurs Slug")
    lesson_id = models.IntegerField(default=1, verbose_name="Dars Raqami")
    content = models.TextField(blank=True, verbose_name="Konspekt Matni")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Oxirgi tahrir")

    class Meta:
        verbose_name = "Dars Konspekti"
        verbose_name_plural = "Dars Konspektlari"
        unique_together = ('user', 'category_slug', 'lesson_id')

    def __str__(self):
        return f"{self.user.username} - {self.category_slug} (Dars #{self.lesson_id})"


class LessonQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lesson_questions")
    student_name = models.CharField(max_length=150, blank=True, verbose_name="O'quvchi Ismi")
    group_name = models.CharField(max_length=50, blank=True, default="FN-24", verbose_name="Guruhi")
    category_slug = models.CharField(max_length=50, verbose_name="Kurs Slug")
    lesson_id = models.IntegerField(default=1, verbose_name="Dars Raqami")
    question = models.TextField(verbose_name="Savol")
    answer = models.TextField(blank=True, verbose_name="Ustoz Javobi")
    answered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="answered_questions")
    answered_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Dars Savoli (Q&A)"
        verbose_name_plural = "Dars Savollari (Q&A)"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.student_name or self.user.username}: {self.question[:40]}..."


class Announcement(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="announcements")
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    content = models.TextField(verbose_name="E'lon Matni")
    target_group = models.CharField(max_length=50, default="all", verbose_name="Mo'ljallangan Guruh (all yoki guruh kodi)")
    is_pinned = models.BooleanField(default=False, verbose_name="Qadalganmi?")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "E'lon"
        verbose_name_plural = "E'lonlar"
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.target_group}] {self.title}"


class DirectionChangeRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', "Kutilmoqda"),
        ('approved', "Qabul qilindi"),
        ('rejected', "Rad etildi"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='direction_requests')
    requested_direction = models.CharField(max_length=100, verbose_name="So'ralgan Yo'nalish")
    requested_direction_slug = models.CharField(max_length=50, verbose_name="Yo'nalish Slug")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Holat")
    teacher = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='direction_approvals')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Yo'nalish O'zgartirish So'rovi"
        verbose_name_plural = "Yo'nalish O'zgartirish So'rovlari"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} -> {self.requested_direction} ({self.get_status_display()})"


class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="certificates")
    certificate_id = models.CharField(max_length=64, unique=True, verbose_name="Sertifikat ID (kod)")
    full_name = models.CharField(max_length=200, verbose_name="Talaba F.I.Sh")
    direction = models.CharField(max_length=150, verbose_name="Tamomlangan Yo'nalish")
    direction_slug = models.CharField(max_length=100, verbose_name="Yo'nalish Slug")
    avg_score = models.DecimalField(max_digits=4, decimal_places=1, default=10.0, verbose_name="O'rtacha Ball")
    issued_at = models.DateTimeField(auto_now_add=True, verbose_name="Berilgan Vaqt")

    class Meta:
        verbose_name = "Sertifikat"
        verbose_name_plural = "Sertifikatlar"
        ordering = ['-issued_at']

    def __str__(self):
        return f"Sertifikat #{self.certificate_id} - {self.full_name}"



