from rest_framework import permissions

class IsArtistOwner(permissions.BasePermission):
    """
    Custom permission to only allow the owner of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the object.
        return obj.artist == request.user.artist