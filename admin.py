from django.contrib import admin
from .models import Category, Course, TypingScore, UserVideoUnlock, HomeworkSubmission, UserProfile

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'icon')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'youtube_id', 'instructor_name', 'level', 'rating')
    list_filter = ('category', 'level', 'created_at')
    search_fields = ('title', 'description', 'instructor_name')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(TypingScore)
class TypingScoreAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'wpm', 'accuracy', 'mode', 'time_limit', 'user', 'created_at')
    list_filter = ('mode', 'time_limit', 'created_at')
    search_fields = ('player_name', 'user__username', 'user__first_name')
    ordering = ('-wpm', '-accuracy', '-created_at')
    readonly_fields = ('created_at',)

@admin.register(UserVideoUnlock)
class UserVideoUnlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category_slug', 'lesson_id', 'unlocked_for_all_users', 'unlocked_by', 'created_at')
    list_filter = ('unlocked_for_all_users', 'category_slug', 'created_at')
    search_fields = ('user__username', 'user__email', 'category_slug')

@admin.register(HomeworkSubmission)
class HomeworkSubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category_slug', 'lesson_id', 'status', 'submitted_at')
    list_filter = ('status', 'category_slug', 'submitted_at')
    search_fields = ('user__username', 'user__email', 'category_slug', 'text_content', 'github_link')
    readonly_fields = ('submitted_at',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'group_name', 'direction', 'approval_status')
    list_filter = ('role', 'group_name', 'approval_status')
    search_fields = ('user__username', 'user__first_name', 'user__email')
