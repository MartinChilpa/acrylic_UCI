from catalog.models import Track
from django.core.management.base import BaseCommand
from django.conf import settings
from catalog.models import Track
from chartmetric.tasks import load_chartmetric_ids


class Command(BaseCommand):
    help = 'Loads Chartmetrics IDs for Tracks and Artists based on ISRCs'
    def handle(self, *args, **options):

        for track in Track.objects.filter(chartmetric_id='').order_by('?'):
            load_chartmetric_ids.delay(track.id)
