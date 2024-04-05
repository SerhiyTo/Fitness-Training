from typing import Dict, Any

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from api.users.models import UserProfile, CoachProfile


class BaseTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user: UserProfile | CoachProfile) -> Token:
        token = super(BaseTokenObtainPairSerializer, cls).get_token(user)
        token["email"] = user.email
        return token

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)
        if (
            not UserProfile.objects.filter(id=self.user.id).exists()
            and not CoachProfile.objects.filter(id=self.user.id).exists()
        ):
            raise serializers.ValidationError({"user": "User does not exist"})
        return data


class ProfileBaseSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
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

    def create(self, validated_data):
        email = validated_data.get("email")
        validated_data.pop("password_repeat")
        user = self.Meta.model.objects.create(username=email, **validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserProfileSerializer(ProfileBaseSerializer):
    class Meta:
        model = UserProfile
        fields = ProfileBaseSerializer.Meta.fields + [
            "height",
            "weight",
        ]


class CoachProfileSerializer(ProfileBaseSerializer):
    class Meta:
        model = CoachProfile
        fields = ProfileBaseSerializer.Meta.fields + [
            "experience",
            "rating",
            "price",
            "specialization",
        ]
