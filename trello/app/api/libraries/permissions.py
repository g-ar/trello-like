from rest_framework import permissions

from app.models import Users
from app.api.constants import *

class IsAuthenticatedOrCreate(permissions.BasePermission):
    SAFE_METHODS = [HTTP_METHOD_POST, HTTP_METHOD_DELETE]
    def has_permission(self, request, view):
        return ( request.method in IsAuthenticatedOrCreate.SAFE_METHODS or request.user and request.user.is_authenticated() )

