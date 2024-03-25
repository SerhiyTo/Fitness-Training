from django.db import models
from django.utils.translation import gettext_lazy as _

from api.users.models import UserProfile, CoachProfile


class TrainingPlan(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="training_plan_user")
    coach = models.ForeignKey(
        CoachProfile, on_delete=models.CASCADE, related_name="training_plan_coach"
    )

    class Meta:
        verbose_name = _("Training Plan")
        verbose_name_plural = _("Training Plans")

    def __str__(self):
        return f"{self.user} - {self.coach}"


class Training(models.Model):
    training_plan = models.ForeignKey(
        TrainingPlan, on_delete=models.CASCADE, related_name="trainings"
    )
    fitness_exercise = models.IntegerField(verbose_name=_("training__fitness_exercise"))
    days_of_week = models.CharField(
        max_length=100, verbose_name=_("training__days_of_week")
    )

    class Meta:
        verbose_name = _("Training")
        verbose_name_plural = _("Trainings")

    def __str__(self):
        return f"{self.training_plan} - {self.fitness_exercise}"


class FitnessExercise(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("fitness_exercise__name"))
    description = models.TextField(verbose_name=_("fitness_exercise__description"))
    video_link = models.URLField(verbose_name=_("fitness_exercise__video_link"))
    image_link = models.URLField(verbose_name=_("fitness_exercise__image_link"))
    exercise_type = models.CharField(
        max_length=100, verbose_name=_("fitness_exercise__exercise_type")
    )
    difficulty = models.CharField(
        max_length=100, verbose_name=_("fitness_exercise__difficulty")
    )
    muscle_group = models.CharField(
        max_length=100, verbose_name=_("fitness_exercise__muscle_group")
    )
    equipment = models.CharField(
        max_length=100, verbose_name=_("fitness_exercise__equipment")
    )
    duration = models.IntegerField(verbose_name=_("fitness_exercise__duration"))
    calories = models.IntegerField(verbose_name=_("fitness_exercise__calories"))
    rating = models.FloatField(verbose_name=_("fitness_exercise__rating"))
    training = models.ManyToManyField(Training, related_name="fitness_exercises")

    class Meta:
        verbose_name = _("Fitness Exercise")
        verbose_name_plural = _("Fitness Exercises")

    def __str__(self):
        return self.name
