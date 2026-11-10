from django.apps import AppConfig
import os
import sys


class CoursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Courses'

    def ready(self):
        # Faqat asosiy dastur yuklanganda bot listenerni ishga tushirish
        if 'runserver' in sys.argv or 'manage.py' not in sys.argv or os.environ.get('RUN_MAIN') == 'true':
            try:
                from .telegram_bot import start_bot_background_listener
                start_bot_background_listener()
            except Exception:
                pass
