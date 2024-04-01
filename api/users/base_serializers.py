from typing import Dict, Any

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from api.users.models import UserProfile


class BaseTokenObtainPairSerializer(TokenObtainPairSerializer):
    profile_model = None

    @classmethod
    def get_token(cls, user: UserProfile) -> Token:
        token = super(BaseTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)
        if not self.profile_model.objects.filter(id=self.user.id).exists():
            raise serializers.ValidationError({"user": "User does not exist"})
        return data


class ProfileSerializer(serializers.ModelSerializer):
    password_repeat = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = None
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "birth_date",
            "password",
            "password_repeat",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password_repeat']:
            raise serializers.ValidationError({'password': 'Password fields did not match.'})
        return attrs

    def create(self, validated_data):
        user = self.Meta.model.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            birth_date=validated_data['birth_date'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
