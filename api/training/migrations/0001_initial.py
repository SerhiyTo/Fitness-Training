# Generated by Django 5.0.3 on 2024-03-25 22:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Training",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fitness_exercise",
                    models.IntegerField(verbose_name="training__fitness_exercise"),
                ),
                (
                    "days_of_week",
                    models.CharField(
                        max_length=100, verbose_name="training__days_of_week"
                    ),
                ),
            ],
            options={
                "verbose_name": "Training",
                "verbose_name_plural": "Trainings",
            },
        ),
        migrations.CreateModel(
            name="FitnessExercise",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, verbose_name="fitness_exercise__name"
                    ),
                ),
                (
                    "description",
                    models.TextField(verbose_name="fitness_exercise__description"),
                ),
                (
                    "video_link",
                    models.URLField(verbose_name="fitness_exercise__video_link"),
                ),
                (
                    "image_link",
                    models.URLField(verbose_name="fitness_exercise__image_link"),
                ),
                (
                    "exercise_type",
                    models.CharField(
                        max_length=100, verbose_name="fitness_exercise__exercise_type"
                    ),
                ),
                (
                    "difficulty",
                    models.CharField(
                        max_length=100, verbose_name="fitness_exercise__difficulty"
                    ),
                ),
                (
                    "muscle_group",
                    models.CharField(
                        max_length=100, verbose_name="fitness_exercise__muscle_group"
                    ),
                ),
                (
                    "equipment",
                    models.CharField(
                        max_length=100, verbose_name="fitness_exercise__equipment"
                    ),
                ),
                (
                    "duration",
                    models.IntegerField(verbose_name="fitness_exercise__duration"),
                ),
                (
                    "calories",
                    models.IntegerField(verbose_name="fitness_exercise__calories"),
                ),
                ("rating", models.FloatField(verbose_name="fitness_exercise__rating")),
                (
                    "training",
                    models.ManyToManyField(
                        related_name="fitness_exercises", to="training.training"
                    ),
                ),
            ],
            options={
                "verbose_name": "Fitness Exercise",
                "verbose_name_plural": "Fitness Exercises",
            },
        ),
        migrations.CreateModel(
            name="TrainingPlan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "coach",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="training_plan_coach",
                        to="users.coachprofile",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="training_plan_user",
                        to="users.userprofile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Training Plan",
                "verbose_name_plural": "Training Plans",
            },
        ),
        migrations.AddField(
            model_name="training",
            name="training_plan",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="trainings",
                to="training.trainingplan",
            ),
        ),
    ]
