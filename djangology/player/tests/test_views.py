from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from player.models import Users

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='password', userDisplayName='Test User')

    def test_log_in(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password'})
        self.assertEqual(response.status_code, 302)

        response = self.client.get(response.url)
        self.assertEqual(response.status_code, 200)

    def test_sign_up(self):
        response = self.client.post(reverse('sign_up'), {'username': 'newuser', 'password': 'newpassword', 'displayname': 'New User'})
        self.assertEqual(response.status_code, 302)

        response = self.client.get(response.url)
        self.assertEqual(response.status_code, 200)


