from rest_framework import serializers

from api.training.models import FitnessExercise, Training, TrainingPlan
from api.users.models import CoachProfile, UserProfile


class TrainingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingPlan
        fields = [
            "user",
            "coach",
        ]

    def validate(self, attrs):
        if not UserProfile.objects.filter(id=attrs["user"]).exists():
            raise serializers.ValidationError({"user": "User does not exist"})
        if not CoachProfile.objects.filter(id=attrs["coach"]).exists():
            raise serializers.ValidationError({"coach": "Coach does not exist"})
        return attrs


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = [
            "training_plan",
            "fitness_exercise",
            "days_of_week",
        ]

    def validate(self, attrs):
        if not TrainingPlan.objects.filter(id=attrs["training_plan"]).exists():
            raise serializers.ValidationError({"training_plan": "Training plan does not exist"})
        return attrs


class FitnessExerciseSerializer(serializers.ModelSerializer):
    training = TrainingSerializer(read_only=True, many=True)

    class Meta:
        model = FitnessExercise
        fields = [
            "name",
            "description",
            "video_link",
            "image_link",
            "exercise_type",
            "difficulty",
            "muscle_group",
            "equipment",
            "duration",
            "calories",
            "rating",
            "training",
        ]
