from rest_framework.permissions import BasePermission

class IsLeader(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'leader'



class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'admin'