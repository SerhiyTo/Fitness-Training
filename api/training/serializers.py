from rest_framework import serializers

from api.training.models import FitnessExercise, Training, TrainingPlan
from api.users.models import UserProfile


class FitnessExerciseSerializer(serializers.ModelSerializer):
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
        ]


class TrainingSerializer(serializers.ModelSerializer):
    fitness_exercises = FitnessExerciseSerializer(many=True)

    class Meta:
        model = Training
        fields = [
            "fitness_exercise",
            "days_of_week",
            "fitness_exercises",
        ]


class TrainingPlanSerializer(serializers.ModelSerializer):
    trainings = TrainingSerializer(many=True)

    class Meta:
        model = TrainingPlan
        fields = [
            "user",
            "trainings",
        ]

    def validate(self, attrs):
        if not UserProfile.objects.filter(id=attrs["user"].id).exists():
            raise serializers.ValidationError({"user": "User does not exist"})
        return attrs

    def create(self, validated_data):
        training_data = validated_data.pop("trainings")
        training_plan = TrainingPlan.objects.create(**validated_data)
        for training in training_data:
            exercises_data = training.pop("fitness_exercises")
            training_instance = Training.objects.create(training_plan=training_plan, **training)
            exercises = [FitnessExercise(**exercise_data) for exercise_data in exercises_data]
            FitnessExercise.objects.bulk_create(exercises)
            training_instance.fitness_exercises.add(*exercises)
        return training_plan
