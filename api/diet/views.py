from rest_framework import generics, mixins, permissions

from api.diet.models import UserDiet
from api.diet.serializers import UserDietSerializer
from api.training.permissions import IsCoach


class UserDietView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [permissions.IsAuthenticated, IsCoach]
    serializer_class = UserDietSerializer
    queryset = UserDiet.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
