from rest_framework import generics, mixins, permissions, status
from rest_framework.response import Response

from api.training.models import TrainingPlan
from api.training.permissions import IsCoach
from api.training.serializers import TrainingPlanSerializer
from api.users.models import CoachProfile


class TrainingPlanView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [permissions.IsAuthenticated, IsCoach]
    serializer_class = TrainingPlanSerializer
    queryset = TrainingPlan.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["coach"] = CoachProfile.objects.get(profile_ptr_id=request.user)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
