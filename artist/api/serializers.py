from rest_framework import serializers
from common.api.pagination import StandardPagination
from artist.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
