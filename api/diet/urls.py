from django.urls import path

from api.diet.views import UserDietView


urlpatterns = [
    path("", UserDietView.as_view(), name="user-diet"),
]
