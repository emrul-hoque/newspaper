from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200) 

    def test_view_url_by_name(self):    
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def SignupPageTests(TestCase):
        username = 'newuser'
        email = 'newuser@email.com'
        password = 'XXXXXXXXXXX'

    def test_signup_page_status_code(self):
        response = self.client.get('/users/signup/')    
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertContains(response, 'Sign Up')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
        self.assertTrue(new_user.is_active)
        self.assertFalse(new_user.is_staff)
        self.assertFalse(new_user.is_superuser)
        self.assertEqual(new_user.get_username(), self.username)
        self.assertEqual(new_user.get_email(), self.email)
        self.assertEqual(new_user.get_full_name(), self.username)
        self.assertEqual(new_user.get_short_name(), self.username)
        self.assertEqual(new_user.get_full_name(), self.username)
        self.assertEqual(new_user.get_short_name(), self.username)