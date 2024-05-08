from elasticsearch_dsl import Q
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.views import TokenObtainPairView

from api.subscription.models import Subscription
from api.subscription.serializers import SubscriptionSerializer
from api.users.documents import CoachProfileDocument
from api.users.models import CoachProfile, UserProfile
from api.users.serializers import (
    BaseTokenObtainPairSerializer,
    CoachProfileSerializer,
    ProfileBaseSerializer,
    UserProfileSerializer,
)


class BaserProfileObtainToken(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BaseTokenObtainPairSerializer


class UserRegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        profile_type = self.request.data.get("profile_type")
        current_serializer = ProfileBaseSerializer
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
    pagination_class = PageNumberPagination

    def get_queryset(self):
        if self.request.query_params:
            filter_params = self.request.query_params.dict()
            search_query = Q("match_all")
            for key, value in filter_params.items():
                search_query &= Q("match", **{key: value})
            return CoachProfileDocument.search().query(search_query).to_queryset()
        return CoachProfileDocument.search().query("match_all").to_queryset()


class SubscriptionUserListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubscriptionSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        user_id = self.request.user.pk
        return Subscription.objects.filter(user=user_id)
