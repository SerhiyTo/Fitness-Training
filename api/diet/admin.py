from django.contrib import admin

from api.diet.models import FoodItem, PortionFood, UserDiet


@admin.register(UserDiet)
class UserDietAdmin(admin.ModelAdmin):
    list_display = ["user", "training", "start_date", "end_date", "price"]


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "image_link",
        "calories",
        "proteins",
        "fats",
        "carbohydrates",
        "rating",
    ]


@admin.register(PortionFood)
class PortionFoodAdmin(admin.ModelAdmin):
    list_display = ["food_item", "portion_size", "user_diet"]
