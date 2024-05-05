from django.urls import path

from api.diet.views import FoodItemView, PortionFoodView, UserDietView


urlpatterns = [
    path("foods/", FoodItemView.as_view(), name="foods"),
    path("portions/", PortionFoodView.as_view(), name="portions"),
    path("", UserDietView.as_view(), name="user-diet"),
]
