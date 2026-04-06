from rest_framework import permissions

class RoleBasedPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Viewers can ONLY use GET/HEAD/OPTIONS
        if request.user.role == 'VIEWER':
            return request.method in permissions.SAFE_METHODS
        
        # Analysts can do everything EXCEPT Delete
        if request.user.role == 'ANALYST':
            return request.method != 'DELETE'
        
        # Admins have full access
        return request.user.role == 'ADMIN'

    def has_object_permission(self, request, view, obj):
        # Users can only see/edit their OWN data, unless they are Admin
        if request.user.role == 'ADMIN':
            return True
        return obj.user == request.user