from django.urls import path

from api.diet.views import FoodItemView, PortionFoodView, UserDietView


urlpatterns = [
    path("food-item/", FoodItemView.as_view(), name="food-item"),
    path("portion-food/", PortionFoodView.as_view(), name="portion-food"),
    path("", UserDietView.as_view(), name="user-diet"),
]
