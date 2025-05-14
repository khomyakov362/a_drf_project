from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.decorators.cache import never_cache

from users.apps import UsersConfig
from users import views

app_name = UsersConfig.name

urlpatterns = [
    path('', views.ListAPIView.as_view(), name='list'),
    path('create/', never_cache(views.CreateAPIView.as_view()), name='create'),
    path('<int:pk>/', views.RetrieveAPIView.as_view(), name='detail'),
    path('<int:pk>/update/', never_cache(views.UpdateAPIView.as_view()), name='update'),
    path('<int:pk>/delete/', never_cache(views.DestroyAPIView.as_view()), name='delete'),
    path('token/', TokenObtainPairView.as_view(), name='token_refresh'),
]