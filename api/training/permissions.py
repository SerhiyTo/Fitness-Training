from rest_framework import permissions

from api.users.models import CoachProfile


class IsCoach(permissions.BasePermission):
    """
    Allows access only to coach user's type.
    """

    def has_permission(self, request, view):
        return CoachProfile.objects.filter(profile_ptr_id=request.user).exists()
