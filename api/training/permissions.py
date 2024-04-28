from rest_framework import permissions

from api.users.models import Profile


class IsCoach(permissions.BasePermission):
    """
    Allows access only to coach user's type.
    """

    def has_permission(self, request, view):
        return request.user.profile_type == Profile.ProfileType.COACH
