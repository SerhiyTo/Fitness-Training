# Generated by Django 5.0.3 on 2024-03-26 00:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("training", "0001_initial"),
        ("users", "0003_alter_profile_birth_date_alter_profile_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="FoodItem",
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
                    models.CharField(max_length=100, verbose_name="food_item__name"),
                ),
                ("image_link", models.URLField(verbose_name="food_item__image_link")),
                ("calories", models.IntegerField(verbose_name="food_item__calories")),
                ("proteins", models.FloatField(verbose_name="food_item__proteins")),
                ("fats", models.FloatField(verbose_name="food_item__fats")),
                (
                    "carbohydrates",
                    models.FloatField(verbose_name="food_item__carbohydrates"),
                ),
                ("rating", models.FloatField(verbose_name="food_item__rating")),
            ],
            options={
                "verbose_name": "Food Item",
                "verbose_name_plural": "Food Items",
            },
        ),
        migrations.CreateModel(
            name="UserDiet",
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
                ("start_date", models.DateField(verbose_name="user_diet__start_date")),
                ("end_date", models.DateField(verbose_name="user_diet__end_date")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="user_diet__price"
                    ),
                ),
                (
                    "training",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_diet",
                        to="training.trainingplan",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_diet",
                        to="users.userprofile",
                    ),
                ),
            ],
            options={
                "verbose_name": "User Diet",
                "verbose_name_plural": "User Diets",
            },
        ),
        migrations.CreateModel(
            name="PortionFood",
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
                    "portion_size",
                    models.FloatField(
                        max_length=100, verbose_name="portion_food__portion_size"
                    ),
                ),
                (
                    "food_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="portions",
                        to="diet.fooditem",
                    ),
                ),
                (
                    "user_diet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="portion_foods",
                        to="diet.userdiet",
                    ),
                ),
            ],
            options={
                "verbose_name": "Portion Food",
                "verbose_name_plural": "Portion Foods",
            },
        ),
    ]
