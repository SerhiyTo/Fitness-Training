from django.urls import path

from api.training.views import FitnessExerciseView, TrainingPlanView, TrainingView


urlpatterns = [
    path("fitness-exercise/", FitnessExerciseView.as_view(), name="fitness_exercise"),
    path("training-session/", TrainingView.as_view(), name="training"),
    path("training-plan/", TrainingPlanView.as_view(), name="training_plan"),
]
