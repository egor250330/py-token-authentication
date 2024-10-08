from django.views import View
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return bool(
            (request.method in SAFE_METHODS and request.user.is_authenticated)
            or request.user.is_staff
        )
