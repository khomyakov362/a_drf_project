from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer, AuthUser
from rest_framework_simplejwt.tokens import Token

from users.validators import PasswordValidator
from users.models import User

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'last_name', 'first_name', 'phone', 'is_active']

class CreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8, max_length=16)

    class Meta:
        model = User
        fields = ['email', 'password']
        validators = [
            PasswordValidator(field='password')
        ]
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()
        return user

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'password' 'phone', 'is_active']
        validators = [
            PasswordValidator(field='password')
        ]

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance.set_password(password)
        instance.save()
        return instance

class TokenObtainPairSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token