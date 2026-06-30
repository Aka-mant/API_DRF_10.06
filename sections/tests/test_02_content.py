from rest_framework.test import APITestCase
from rest_framework import status

from  sections.tests.utils import get_member_user, get_admin_user, get_test_content

class ContentTestAdmin(APITestCase):
    def setUp(self):
        self.admin_user = get_admin_user()
        response = self.client.post('/users/token/', {'email': self.admin_user.email, 'password': "12346789"}, format='json')
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        self.content = get_test_content()


    def test_08_content_create(self):
        data = {
            "section": self.content.section.id,
            "title": "Test content title create",
            "content": "Test content create",
        }
        response = self.client.post('/content/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('title'), data['title'])
        self.assertEqual(response.json().get('content'), data['content'])


    def test_09_content_detail(self):
        response = self.client.get(f'/content/{self.content.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), self.content.title)
        self.assertEqual(response.json().get('content'), self.content.content)


    def test_10_content_update(self):
        data = {
            "title": "Test content title Patch",


        }
        response = self.client.patch(f'/content/{self.content.id}/update/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), "Test content title Patch")


    def test_11_content_delete(self):
        response = self.client.delete(f'/content/{self.content.id}/delete/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(f'/content/{self.content.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_12_content_list(self):
        response = self.client.get('/content/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['title'], self.content.title)

    def test_23_str_content(self):
        self.assertEqual(str(self.content), 'Test Title Content')



class ContentTestMember(APITestCase):
    def setUp(self):
        self.member_user = get_member_user()
        response = self.client.post('/users/token/', {'email': self.member_user.email, 'password': "12346789"}, format='json')
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.content = get_test_content()

    def test_13_content_create_forbidden(self):
        data = {
            "section": self.content.section.id,
            "title": "Test content title create Forbidden",
            "content": "Test content create Forbidden",
        }
        response = self.client.post('/content/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json().get('detail'), "У вас недостаточно прав для выполнения данного действия.")

    def test_14_content_update_forbidden(self):
        data = {
            "title": "Test content title Patch Forbidden",
        }
        response = self.client.patch(f'/content/{self.content.id}/update/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json().get('detail'), "У вас недостаточно прав для выполнения данного действия.")

    def test_15_content_delete_forbidden(self):
        response = self.client.delete(f'/content/{self.content.id}/delete/', format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json().get('detail'), "You must be a superuser to perform this action.")



