from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class UserRegistrationAPIViewTestCase(APITestCase):
    def test_registration(self):
        url = reverse("user_view")
        user_data = {
            "nickname": "nickname1", # 최소 한 개의 영문자와 숫자를 포함해 5글자 이상 닉네임을 입력
            "email": "test@testuser.com",
            "password": "password1", # 동일한 비밀번호 입력
            "password_check": "password1", # 동일한 비밀번호 입력
        }
        response = self.client. post(url, user_data)
        self.assertEqual(response.status_code, 201) # 테스트 성공완료