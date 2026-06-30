from rest_framework.test import APITestCase
from rest_framework import status

from sections.tests.utils import get_admin_user
from users.models import User


class UserTestCase(APITestCase):
    def setUp(self):
        self.admin_user = get_admin_user()
        self.manager = User.objects
        response = self.client.post('/users/token/', {'email': self.admin_user.email, 'password': "12346789"},
                                    format='json')
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_18_str_username(self):
        self.assertEqual(str(self.admin_user), 'example45@example.com')

    def test_19_create_user_without_email_raise_error(self):
        with self.assertRaises(ValueError):
            self.manager.create_user(email=None, password="123456789")

    def test_20_email_normalization(self):

        user = self.manager.create_user(
            email='  TeSt@ExAmPle.CoM  ',
            password='password123'
        )
        self.assertEqual(user.email, 'test@example.com')


    def test_21_create_user_creates_active_non_staff_non_superuser(self):


        user = self.manager.create_user(
            email='normal@example.com',
            password='password123',
        )
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        self.assertNotEqual(user.password, 'password123')
        self.assertTrue(user.check_password('password123'))

    def test_21_create_superuser_sets_flags_correctly(self):
        user = self.manager.create_superuser(
            email='super@example.com',
            password='password123',
        )
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.check_password('password123'))
