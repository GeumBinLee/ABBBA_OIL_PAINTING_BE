from django.urls import reverse 
from rest_framework.test import APITestCase 


class UserRegistrationAPIViewTestCase(APITestCase):     
    def test_registration(self):
        url = reverse("user_view")                      
        user_data = {                                   
        "nickname": "nickname1",                        
        "email": "test@testuser.com",                   
        "password": "password1",                        
        "password_check": "password1",                  
        }                                               
        response = self.client.post(url, user_data)     # url 및 user 데이터 가져오기
        self.assertEqual(response.status_code, 201)
        
        
    def test_registration_failed(self):
        url = reverse("user_view")                     
        user_data = {                                   
        "nickname": "nickname1",                        
        "email": "test@testuser.com",                   
        "password": "password1",                        
        "password_check": "password!",
        }                                               
        response = self.client.post(url, user_data)     # url 및 user 데이터 가져오기
        self.assertEqual(response.status_code, 400)