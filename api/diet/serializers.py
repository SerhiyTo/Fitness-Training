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
    food_item = FoodItemSerializer(many=True)

    class Meta:
        model = PortionFood
        fields = ["food_item", "portion_size"]


class UserDietSerializer(serializers.ModelSerializer):
    portion_foods = PortionFoodSerializer(many=True)

    class Meta:
        model = UserDiet
        fields = ["user", "training", "start_date", "end_date", "price", "portion_foods"]

    def validate(self, attrs):
        if attrs["start_date"] > attrs["end_date"]:
            raise serializers.ValidationError("End date must be greater than start date")
        if not UserProfile.objects.filter(id=attrs["user"].id).exists():
            raise serializers.ValidationError({"user": "User does not exist"})
        return attrs

    def create(self, validated_data):
        portion_foods_data = validated_data.pop("portion_foods")
        user_diet = UserDiet.objects.create(**validated_data)
        for portion_food_data in portion_foods_data:
            food_data = portion_food_data.pop("food_item")
            portion_food = PortionFood.objects.create(user_diet=user_diet, **portion_food_data)
            food_items = [FoodItem(**food_data) for food_data in food_data]
            FoodItem.objects.bulk_create(food_items)
            portion_food.food_item.add(*food_items)
        return user_diet
