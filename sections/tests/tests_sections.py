from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from sections.models import Section 
from sections.tests.utils import create_admin_user, create_member_user

class SectionTestCase(APITestCase):

    def setUp(self):
        self.user = create_admin_user()
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
            'description' : 'Test Description Create'
        }
        response = self.client.post('/section/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('description'), 'Test Description Create')
        self.assertEqual(response.json().get('title'), 'Test Section Create')

    def test_02_section_detail(self):
        response = self.client.get('/section/3/')
        self.assertEqual(response.json().get('description'), 'Test Description')
        self.assertEqual(response.json().get('title'), 'Test Section')
    
    def test_03_section_update(self):
        data = {
            'title' : 'Test Section Update Put',
            'description' : 'Test Description Update Put'
        }
        response = self.client.put('/section/4/update/', data=data)
        self.assertEqual(response.json().get('description'), 'Test Description Update Put')
        self.assertEqual(response.json().get('title'), 'Test Section Update Put')
    
    def test_04_section_delete(self):
        response = self.client.delete('/section/5/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_05_section_list(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('results'), [{'id': 6, 'title': 'Test Section', 'content_title': []}])
    
    def test_06_section_create_forbidden(self):
        create_member_user()
        member_client = APIClient()
        response = member_client.post('/users/token/', {'email' : 'test_member@mail.com', 'password' : 'querty'})
        member_access_token = response.json().get('access')
        member_client.credentials(HTTP_AUTHORIZATION=f'Bearer {member_access_token}')
        data = {
            'title' : 'Test Section Forbidden'
        } 
        response = member_client.post('/section/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)







