from catalog.models import *
from chartmetric.engine import *
from django.core.management.base import BaseCommand
from django.conf import settings
from artist.models import Artist
from catalog.models import Track



class Command(BaseCommand):
    help = 'Loads Chartmetrics IDs for Tracks and Artists based on ISRCs'
    def handle(self, *args, **options):

        cm = Chartmetric()
        cm.authenticate()

        for track in Track.objects.filter(chartmetric_id='').order_by('?'):
            data = cm.get_track_artist_ids_from_isrc(track.isrc)
            if len(data['obj']['tracks']) > 0:
                track.chartmetric_id = data['obj']['tracks'][0]['id']
                print(f'Track: {track.chartmetric_id}')
                if not track.artist.chartmetric_id:
                    artist = track.artist
                    artist.chartmetric_id = data['obj']['tracks'][0]['artist'][0]['id']
                    artist.save()
                    print(f'Artist: {artist.chartmetric_id}')
                track.save()
