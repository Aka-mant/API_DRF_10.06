import django
from  rest_framework.test import APITestCase
from rest_framework import status

django.setup()

from sections.tests.utils import get_member_user, get_admin_user, get_test_section

class SectionTests(APITestCase):
    def setUp(self):
        self.admin_user = get_admin_user()
        response = self.client.post('/users/token/', {'email': self.admin_user.email, 'password': "12346789"}, format='json')
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_section = get_test_section()

    def test_01_section_create(self):
        data = {
            'title': 'Test Section Create',
            "description": "This is a test description create",

        }
        response = self.client.post('/sections/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])

        self.assertEqual(response.data['description'], data['description'])

    def test_02_section_detail(self):
        response = self.client.get(f'/sections/{self.test_section.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], str(self.test_section.title))
        self.assertEqual(response.data['description'], str(self.test_section.description))

    def test_03_section_update(self):
        data = {
            'title': 'Test Section Update PUT',
            "description": "This is a test description update PUT",
        }
        response = self.client.put(f'/sections/{self.test_section.id}/update/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['description'], data['description'])

    def test_04_section_delete(self):
        response = self.client.delete(f'/sections/{self.test_section.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(f'/sections/{self.test_section.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_05_section_list(self):
        response = self.client.get('/sections/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['title'], str(self.test_section.title))

    def test_22_section_str_name(self):
        self.assertEqual(str(self.test_section), 'Test Section')





class SectionTestsMember(APITestCase):
    def setUp(self):
        self.member_user = get_member_user()
        response = self.client.post('/users/token/', {'email': self.member_user.email, 'password': "12346789"}, format='json')
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_section = get_test_section()

    def test_06_section_create_forbidden(self):
        data = {
            'title': 'Test Section Create Forbidden',
            "description": "This is a test description create Forbidden",
        }
        response = self.client.post('/sections/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json().get('detail'), 'У вас недостаточно прав для выполнения данного действия.')

    def test_07_section_delete_forbidden(self):
        response = self.client.delete(f'/sections/{self.test_section.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json().get('detail'), 'You must be a superuser to perform this action.')






