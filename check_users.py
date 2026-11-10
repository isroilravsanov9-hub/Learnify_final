import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Learnify.settings')
django.setup()

from django.contrib.auth.models import User

print("Total users in DB:", User.objects.count())
for u in User.objects.all():
    print(f"- id: {u.id}, username: {u.username}, role: {getattr(u, 'userprofile', None)}")
