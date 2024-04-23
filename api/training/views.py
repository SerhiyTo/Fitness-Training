from rest_framework import generics, mixins, permissions

from api.training.models import FitnessExercise, Training, TrainingPlan
from api.training.permissions import IsCoach
from api.training.serializers import FitnessExerciseSerializer, TrainingPlanSerializer, TrainingSerializer


class FitnessExerciseView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsCoach]
    serializer_class = FitnessExerciseSerializer
    queryset = FitnessExercise.objects.all()


class TrainingView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsCoach]
    serializer_class = TrainingSerializer
    queryset = Training.objects.all()


class TrainingPlanView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [permissions.IsAuthenticated, IsCoach]
    serializer_class = TrainingPlanSerializer
    queryset = TrainingPlan.objects.all()
