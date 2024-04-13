from rest_framework import generics, permissions, status
from rest_framework.response import Response

from api.subscription.models import Subscription
from api.subscription.serializers import SubscriptionSerializer
from api.users.models import UserProfile


class SubscriptionView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_profile = UserProfile.objects.get(id=self.request.user.pk)
        serializer.save(user=user_profile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SubscriptionListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        user_id = self.request.user.pk
        return Subscription.objects.filter(user=user_id)
