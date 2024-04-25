from django.urls import path

from api.training.views import TrainingPlanView


urlpatterns = [
    path("", TrainingPlanView.as_view(), name="training"),
]
