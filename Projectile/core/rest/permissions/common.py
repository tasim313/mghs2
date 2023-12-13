from rest_framework.permissions import BasePermission


class CommonPermission(BasePermission):
    message = "Access Denied! You Don't have permission to edit or delete"

    def has_permission(self, request, view):
        if request.method in ['GET', 'POST', 'DELETE', 'PUT', 'PATCH', 'OPTIONS']:
            return True
        return False
        
    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return True

        if request.method == 'POST':
            if request.user.role == 'Admin':
                return True
            if request.user.role == 'Manager':
                return True
            if request.user.role == 'hr':
                return True
            if request.user.role == 'accounts':
                return True
            return False
        
        if request.method == 'PATCH':
            if request.user.role == 'Admin':
                return True
            if request.user.role == 'Manager':
                return True
            if request.user.role == 'hr':
                return True
            if request.user.role == 'accounts':
                return True
            return False
        
        if request.method == 'PUT':
            if request.user.role == 'Admin':
                return True
            if request.user.role == 'Manager':
                return True
            if request.user.role == 'hr':
                return True
            if request.user.role == 'accounts':
                return True
            return False
        
        if request.method == 'DELETE':
            if request.user.role == 'Admin':
                return True
            if request.user.role == 'Manager':
                return False
            if request.user.role == 'hr':
                return False
            if request.user.role == 'accounts':
                return False
            return False
    
        if request.method == 'OPTIONS':
            if request.user.role == 'Admin':
                return True
            if request.user.role == 'Manager':
                return True
            if request.user.role == 'hr':
                return True
            if request.user.role == 'accounts':
                return True
            return False
        
        
        return False
