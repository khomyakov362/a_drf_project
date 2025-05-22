from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from sections.models import Section, SectionContent
from sections.tests.utils import create_admin_user, create_member_user

class SectionContentTestCase(APITestCase):

    def setUp(self):
        self.user = create_admin_user()
        response = self.client.post('/users/token/', {'email' : 'test_admin@mail.com', 'password' : 'qwerty'})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.test_section = Section.objects.create(
            title='Test Section',
            description='Test Description'
        )

        self.test_section_content = SectionContent.objects.create(
            section=self.test_section,
            title='Test Section Content Title',
            content='Test Section Content'
        )
    
    def test_01_content_create(self):
        data = {
            'section': self.test_section.pk,
            'title': 'Test Title Create',
            'content': 'Test Content Create'
        }
        response = self.client.post('/content/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('title'), 'Test Title Create')
        self.assertEqual(response.json().get('content'), 'Test Content Create')

    def test_02_content_detail(self):
        response = self.client.get(f'/content/{self.test_section_content.pk}/')
        self.assertEqual(response.json().get('section'), self.test_section.pk)
        self.assertEqual(response.json().get('title'), 'Test Section Content Title')
        self.assertEqual(response.json().get('content'), 'Test Section Content')
    
    def test_03_content_update(self):
        data = {
            'section' : self.test_section.pk,
            'title' : 'Test Section Content Update Put',
            'content' : 'Test Description Content Update Put'
        }
        response = self.client.put(f'/content/{self.test_section_content.pk}/update/', data=data)
        self.assertEqual(response.json().get('title'), 'Test Section Content Update Put')
        self.assertEqual(response.json().get('content'), 'Test Description Content Update Put')
    
    def test_04_content_delete(self):
        response = self.client.delete(f'/content/{self.test_section_content.pk}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_05_content_list(self):
        response = self.client.get('/content/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('results'), [{'id': self.test_section_content.pk, 'section': 'Test Section', 'title': 'Test Section Content Title'}])
    
    def test_06_content_create_forbidden(self):
        create_member_user()
        member_client = APIClient()
        response = member_client.post('/users/token/', {'email' : 'test_member@mail.com', 'password' : 'querty'})
        member_access_token = response.json().get('access')
        member_client.credentials(HTTP_AUTHORIZATION=f'Bearer {member_access_token}')
        data = {
            'title' : 'Test Content Forbidden',
            'section' : self.test_section.pk
        } 
        response = member_client.post('/content/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)