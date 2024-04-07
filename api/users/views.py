from rest_framework import permissions, generics
from rest_framework_simplejwt.views import TokenObtainPairView

from api.users.models import UserProfile, CoachProfile
from api.users.serializers import BaseTokenObtainPairSerializer, UserProfileSerializer, CoachProfileSerializer
from api.users.utils import query_params_to_dict


class BaserProfileObtainToken(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BaseTokenObtainPairSerializer


class UserRegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        profile_type = self.request.data.get('profile_type')
        current_serializer = None
        if profile_type == "user":
            current_serializer = UserProfileSerializer
        elif profile_type == "coach":
            current_serializer = CoachProfileSerializer
        return current_serializer

    def get_queryset(self):
        if "height" and "weight" in self.request.data:
            return UserProfile.objects.all()
        return CoachProfile.objects.all()


class CoachListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CoachProfileSerializer

    def get_queryset(self):
        if self.request.query_params:
            filter_params = query_params_to_dict(self.request.query_params)
            return CoachProfile.objects.filter(**filter_params)
        return CoachProfile.active.all()
