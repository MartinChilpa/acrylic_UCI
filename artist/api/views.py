from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.api.pagination import StandardPagination
from artist.api.serializers import ArtistSerializer
from artist.models import Artist


class ArtistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Artist.active.all()
    serializer_class = ArtistSerializer
    pagination_class = StandardPagination
    