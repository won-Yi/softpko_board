from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        # password 해싱작업
        password = user.password
        user.set_password(password) 
        user.save()
        return user

    def update(self, validated_data):
        user = super().create(validated_data)
        # password 해싱작업
        password = user.password
        user.set_password(password) 
        user.save()
        return user


class CustomTokenObtainPairserializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email

        return token