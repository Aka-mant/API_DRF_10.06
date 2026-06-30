from django.utils.translation import gettext_lazy as _

from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    message = _('You must be a moderator to perform this action.')

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsSuperuser(BasePermission):
    message = _('You must be a superuser to perform this action.')

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        return False
