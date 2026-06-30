from rest_framework.test import APITestCase
from rest_framework import status


from sections.tests.utils import get_test_question, get_member_user


class QuestionTest(APITestCase):
    def setUp(self):
        self.member_user = get_member_user()
        response = self.client.post('/users/token/', {'email': self.member_user.email, 'password': "12346789"}, format='json')
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.question = get_test_question()

    def test_16_question_list(self):
        response = self.client.get('/questions/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['question'], "This is a test question")

    def test_17_question_detail(self):
        response = self.client.get(f'/questions/{self.question.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json().get('question'), "This is a test question")

    def test_18_question_is_correct(self):
        correct_answer = {
            "member_answer": "Test Title Content",

        }
        wrong_answer = {
            "member_answer": "Wrong Title Content",
        }
        response = self.client.post(f'/questions/{self.question.id}/', correct_answer)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('is_correct'), True)
        response = self.client.post(f'/questions/{self.question.id}/', wrong_answer)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('is_correct'), False)

    def test_24_str_question(self):
        self.assertEqual(str(self.question), f"Вопрос по курсу {self.question.section.title}")
