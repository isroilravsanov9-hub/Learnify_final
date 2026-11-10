from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from Courses.models import Course, Category

class RegistrationAndAuthTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Dasturlash", slug="dasturlash", icon="code")
        self.course = Course.objects.create(
            title="Django Kursi",
            slug="django-kursi",
            category=self.category,
            short_description="Qisqa",
            description="Batafsil",
            instructor_name="Ali Valiyev",
            price=500000
        )

    def test_registration_success(self):
        # Ro'yxatdan o'tish testi
        response = self.client.post(reverse('register'), {
            'full_name': 'Akmal Saidov',
            'email': 'akmal@example.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!'
        })
        
        # Sign-in sahifasiga yo'naltirishi kerak
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)
        self.assertIn('registered=1', response.url)
        self.assertIn('akmal@example.com', response.url)

        # Foydalanuvchi bazada mavjudligini tekshirish
        user = User.objects.filter(email='akmal@example.com').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.first_name, 'Akmal Saidov')

    def test_registration_ajax(self):
        # AJAX orqali ro'yxatdan o'tish
        response = self.client.post(reverse('register'), {
            'full_name': 'Madina Karimova',
            'email': 'madina@example.com',
            'password': 'SecurePassword123',
            'confirm_password': 'SecurePassword123',
            'ajax': '1'
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertIn('/login/', data['redirect_url'])

    def test_login_after_registration(self):
        # Avval foydalanuvchi yaratamiz
        User.objects.create_user(
            username='user_test',
            email='testuser@example.com',
            password='SecretPassword123',
            first_name='Test User'
        )

        # Email orqali kirish
        response = self.client.post(reverse('login'), {
            'login_input': 'testuser@example.com',
            'password': 'SecretPassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
