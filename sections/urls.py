from django.urls import path
from rest_framework.routers import DefaultRouter

from sections.apps import SectionsConfig
from sections import views

app_name = SectionsConfig.name
router = DefaultRouter()

urlpatterns = [
    path('', views.ListAPIView.as_view(), name='list'),
    path('section/create/', views.CreateAPIView.as_view(), name='create'),
    path('section/<int:pk>/', views.RetrieveAPIView.as_view(), name='detail'),
    path('section/<int:pk>/update/', views.UpdateAPIView.as_view(), name='update'),
    path('section/<int:pk>/delete/', views.DestroyAPIView.as_view(), name='delete'),
    path('content/', views.ContentListAPIView.as_view(), name='content_list'),
    path('content/create/', views.ContentCreateAPIView.as_view(), name='content_create'),
    path('content/<int:pk>/update/', views.ContentUpdateAPIView.as_view(), name='content_update'),
    path('content/<int:pk>/delete/', views.ContentDestroyAPIView.as_view(), name='content_delete'),
    path('content/<int:pk>/', views.ContentRetrieveAPIView.as_view(), name='content_detail'),
    path('questions/',  views.QuestionListAPIView.as_view(), name='question_list'),
    path('questions/<int:pk>/', views.QuestionRestrieveAPIView.as_view(), name='question_detail')
] + router.urls