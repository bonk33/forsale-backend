from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allow to any request,
        # so GET, HEAD, OPTIONS requests are always allowed.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user

class IsStafforTargetUser(permissions.BasePermission):
    """
    Custom permission class for User View
    """
    def has_permission(self, request, view):
        #allow user to list all users if logged in user is staff
        return view.action == 'retrieve' or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        #allow logged in user to view own details, allows staff to view all records
        return request.user.is_staff or obj == request.user
  