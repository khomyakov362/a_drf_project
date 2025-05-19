from rest_framework import generics  
from rest_framework_simplejwt import views
from rest_framework.permissions import IsAuthenticated, AllowAny

from users import serializers
from users.models import User

class ListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.Serializer

class CreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.CreateSerializer
    permission_classes = (AllowAny,)

class RetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.Serializer
    permission_classes = (AllowAny,)

class UpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UpdateSerializer
    permission_classes = (AllowAny,)

    # def get_queryset(self):
    #     user = self.request.user
    #     print(user.id)
    #     return User.objects.filter(id=user.id)

class DestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
