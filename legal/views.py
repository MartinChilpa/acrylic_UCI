from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from catalog.models import Track  # Ensure the correct import path
from legal.models import MasterSplit
from legal.serializers import MyMasterSplitSerializer
from artist.permissions import IsTrackArtistOwner


class MasterSplitViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing, editing and deleting master splits.
    """
    permission_classes = [permissions.IsAuthenticated, IsTrackArtistOwner]
    queryset = MasterSplit.objects.none()
    serializer_class = MyMasterSplitSerializer

    def get_queryset(self):
        """
        This view returns a list of all master splits for a track
        provided by the track's ID passed in the URL.
        """
        track_id = self.kwargs.get('track_id')
        if track_id is not None:
            return self.queryset.filter(track_id=track_id, track__artist=self.request.user.artist)
        return self.queryset.none()  # Return an empty queryset if no track_id is provided

    def perform_create(self, serializer):
        """
        Associate the new master split with a track before saving it.
        """
        track_id = self.kwargs.get('track_id')
        try:
            track = Track.objects.get(id=track_id)
        except Track.DoesNotExist:
            return Response({"error": "Track not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer.save(track=track)

    def perform_update(self, serializer):
        """
        Update a master split, ensuring it is associated with the correct track.
        """
        track_id = self.kwargs.get('track_id')
        try:
            track = Track.objects.get(id=track_id)
        except Track.DoesNotExist:
            return Response({"error": "Track not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer.save(track=track)
