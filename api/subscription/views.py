from rest_framework import generics, mixins, permissions, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.subscription.models import Subscription
from api.subscription.serializers import SubscriptionSerializer
from api.users.models import UserProfile


class SubscriptionView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubscriptionSerializer
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if self.lookup_field in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_profile = UserProfile.objects.get(id=self.request.user.pk)
        serializer.save(user=user_profile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = Subscription.active.all()
        if self.lookup_field in self.kwargs:
            queryset = Subscription.objects.filter(pk=self.kwargs["pk"])
        if self.request.query_params:
            filter_params = self.request.query_params.dict()
            queryset = Subscription.objects.filter(**filter_params)
        return queryset

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
