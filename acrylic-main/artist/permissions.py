from rest_framework import permissions


class IsArtistOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.artist == request.user.artist


class IsTrackArtistOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.track.artist == request.user.artist