from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # Read Permission 은 모두에게 열려있음
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user