from django.contrib import admin
from .models import TrainingPlan, Training, FitnessExercise


@admin.register(TrainingPlan)
class TrainingPlanAdmin(admin.ModelAdmin):
    list_display = ("user", "coach")


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ("training_plan", "fitness_exercise", "days_of_week")


@admin.register(FitnessExercise)
class FitnessExerciseAdmin(admin.ModelAdmin):
    list_display = (
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
    )
