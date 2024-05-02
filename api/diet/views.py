from rest_framework import generics, mixins, permissions

from api.diet.models import FoodItem, PortionFood, UserDiet
from api.diet.serializers import FoodItemSerializer, PortionFoodSerializer, UserDietSerializer
from api.training.permissions import IsCoach


class BaseView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [permissions.IsAuthenticated, IsCoach]
    serializer_class = None
    queryset = None

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class FoodItemView(BaseView):
    serializer_class = FoodItemSerializer
    queryset = FoodItem.objects.all()


class PortionFoodView(BaseView):
    serializer_class = PortionFoodSerializer
    queryset = PortionFood.objects.all()


class UserDietView(BaseView):
    serializer_class = UserDietSerializer
    queryset = UserDiet.objects.all()
