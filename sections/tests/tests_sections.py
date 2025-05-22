from rest_framework.test import APITestCase
from rest_framework import status

from sections.models import Section 
from sections.tests.utils import get_admin_user, get_member_user

class SectionTestCase(APITestCase):

    def setUp(self):
        self.user = get_admin_user()
        response = self.client.post('/users/token/', {'email' : 'test_admin@mail.com', 'password' : 'qwerty'})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        
        self.test_section = Section.objects.create(
            title='Test Section',
            description='Test Description'
        )
    
    def test_01_section_create(self):
        data = {
            'title' : 'Test Section Create',
            'description' : 'Test Description'
        }
        response = self.client.post('/section/create/', data=data)
        print(response.json())



