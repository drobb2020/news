from django.contrib.auth import get_user_model  # type: ignore
from django.test import TestCase  # type: ignore
from django.urls import reverse  # type: ignore


class UserManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            drobb2011@gmail.com="testuser@example.com",
            password="Testing1234",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.drobb2011@gmail.com, "testuser@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="testsuperuser",
            drobb2011@gmail.com="testsuperuser@example.com",
            password="Testing1234",
        )
        self.assertEqual(admin_user.username, "testsuperuser")
        self.assertEqual(admin_user.drobb2011@gmail.com, "testsuperuser@example.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTest(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        response = self.client.post(
            reverse('signup'),
            {
                'username': 'testuser',
                'drobb2011@gmail.com': 'testuser@example.com',
                'password1': 'Testing1234',
                'password2': 'Testing1234',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'testuser')
        self.assertEqual(get_user_model().objects.all()[0].drobb2011@gmail.com, 'testuser@example.com')
