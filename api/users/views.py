from rest_framework import permissions, generics
from rest_framework_simplejwt.views import TokenObtainPairView

from api.users.models import UserProfile, CoachProfile
from api.users.serializers import CoachProfileSerializer, UserProfileObtainPairToken, UserProfileSerializer


class UserProfileObtainToken(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserProfileObtainPairToken


class CoachProfileObtainToken(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CoachProfileSerializer


class UserProfileView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CoachProfileView(generics.CreateAPIView):
    queryset = CoachProfile.objects.all()
    serializer_class = CoachProfileSerializer
