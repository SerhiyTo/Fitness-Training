from typing import Dict, Any

from rest_framework import serializers

from api.subscription.models import Subscription
from api.users.models import CoachProfile, UserProfile


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            "coach",
            "start_date",
            "end_date",
            "price",
        ]

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, Any]:
        data = super().validate(attrs)
        user = self.context["request"].user
        coach = attrs.get("coach")

        if not UserProfile.objects.filter(id=user.id).exists():
            raise serializers.ValidationError({"user": "User does not exist"})

        if not CoachProfile.objects.filter(id=coach.id).exists():
            raise serializers.ValidationError({"coach": "Coach does not exist"})

        if Subscription.objects.filter(user=user, coach=coach).exists():
            raise serializers.ValidationError({"subscription": "Subscription already exists"})

        return data
