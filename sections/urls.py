from django.urls import path
from rest_framework.routers import DefaultRouter

from sections.apps import SectionsConfig
from sections import views

app_name = SectionsConfig.name
router = DefaultRouter()

urlpatterns = [
    path('', views.ListAPIView.as_view(), name='list'),
    path('section/create/', views.CreateAPIView.as_view(), name='create'),
    path('section/<int:pk>/', views.RetrieveAPIView.as_view(), name='retrieve'),
    path('section/<int:pk>/update/', views.UpdateAPIView.as_view(), name='update'),
    path('section/<int:pk>/delete/', views.DestroyAPIView.as_view(), name='delete'),
] + router.urls