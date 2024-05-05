from rest_framework import serializers

from api.diet.models import FoodItem, PortionFood, UserDiet
from api.users.models import UserProfile


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = [
            "name",
            "image_link",
            "calories",
            "proteins",
            "fats",
            "carbohydrates",
            "rating",
        ]


class PortionFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortionFood
        fields = ["food_item", "portion_size", "user_diet"]


class UserDietSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDiet
        fields = ["user", "training", "start_date", "end_date", "price"]

    def validate(self, attrs):
        if attrs["start_date"] > attrs["end_date"]:
            raise serializers.ValidationError("End date must be greater than start date")
        if not UserProfile.objects.filter(id=attrs["user"].id).exists():
            raise serializers.ValidationError({"user": "User does not exist"})
        return attrs
