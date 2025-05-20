from rest_framework import generics, permissions
from rest_framework_simplejwt import views

from sections.views import AUTHENTICATED, ADMIN_OR_MOD
from users import serializers
from users.models import User

ANY = (permissions.AllowAny,)

class ListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.Serializer

class CreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.CreateSerializer
    permission_classes = AUTHENTICATED

class RetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.Serializer
    permission_classes = ANY

class UpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UpdateSerializer
    permission_classes = AUTHENTICATED

    def get_queryset(self):
        user = self.request.user
        print(user.id)
        return User.objects.filter(id=user.id)

class DestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = AUTHENTICATED

    def get_queryset(self):
        user = self.request.user
        print(user.id)
        return User.objects.filter(id=user.id)
