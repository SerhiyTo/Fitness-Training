from django.urls import path, include

urlpatterns = [
    path("users/", include("api.users.urls")),
    path("subscriptions/", include("api.subscription.urls")),
    path("trainings/", include("api.training.urls")),
    path("diets/", include("api.diet.urls")),
]
