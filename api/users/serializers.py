from api.users.base_serializers import ProfileSerializer, BaseTokenObtainPairSerializer
from api.users.models import UserProfile, CoachProfile


class UserProfileObtainPairToken(BaseTokenObtainPairSerializer):
    profile_model = UserProfile


class CoachProfileObtainPairToken(BaseTokenObtainPairSerializer):
    profile_model = CoachProfile


class UserProfileSerializer(ProfileSerializer):
    class Meta(ProfileSerializer.Meta):
        model = UserProfile
        fields = ProfileSerializer.Meta.fields + ["height", "weight"]

    def create(self, validated_data):
        user = self.Meta.model.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            birth_date=validated_data['birth_date'],
            height=validated_data['height'],
            weight=validated_data['weight'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CoachProfileSerializer(ProfileSerializer):
    class Meta(ProfileSerializer.Meta):
        model = CoachProfile
        fields = ProfileSerializer.Meta.fields + [
            "experience",
            "rating",
            "price",
            "specialization",
        ]

    def create(self, validated_data):
        user = self.Meta.model.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            birth_date=validated_data['birth_date'],
            experience=validated_data['experience'],
            rating=validated_data['rating'],
            price=validated_data['price'],
            specialization=validated_data['specialization'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
