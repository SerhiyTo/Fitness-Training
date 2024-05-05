from django.db import models
from django.utils.translation import gettext_lazy as _

from api.training.models import TrainingPlan


class UserDiet(models.Model):
    user = models.ForeignKey("users.UserProfile", on_delete=models.CASCADE, related_name="user_diet")
    training = models.ForeignKey(TrainingPlan, on_delete=models.CASCADE, related_name="user_diet")
    start_date = models.DateField(verbose_name=_("user_diet__start_date"))
    end_date = models.DateField(verbose_name=_("user_diet__end_date"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("user_diet__price"))

    class Meta:
        verbose_name = _("User Diet")
        verbose_name_plural = _("User Diets")

    def __str__(self):
        return f"{self.user} - {self.start_date} - {self.end_date}"


class FoodItem(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("food_item__name"))
    image_link = models.URLField(verbose_name=_("food_item__image_link"))
    calories = models.IntegerField(verbose_name=_("food_item__calories"))
    proteins = models.FloatField(verbose_name=_("food_item__proteins"))
    fats = models.FloatField(verbose_name=_("food_item__fats"))
    carbohydrates = models.FloatField(verbose_name=_("food_item__carbohydrates"))
    rating = models.FloatField(verbose_name=_("food_item__rating"))

    class Meta:
        verbose_name = _("Food Item")
        verbose_name_plural = _("Food Items")

    def __str__(self):
        return self.name


class PortionFood(models.Model):
    food_item = models.ManyToManyField(FoodItem, related_name="portions")
    portion_size = models.FloatField(max_length=100, verbose_name=_("portion_food__portion_size"))
    user_diet = models.ForeignKey(UserDiet, on_delete=models.CASCADE, related_name="portion_foods")

    class Meta:
        verbose_name = _("Portion Food")
        verbose_name_plural = _("Portion Foods")

    def __str__(self):
        return f"{self.food_item.all()} - {self.portion_size}"
