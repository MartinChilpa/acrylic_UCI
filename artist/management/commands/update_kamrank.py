from django.db.models import Max, F, FloatField
from django.db.models.functions import Cast
from django.core.management.base import BaseCommand
from django.conf import settings
from artist.models import Artist


class Command(BaseCommand):
    help = 'Reloads artists KAMRank'

    def handle(self, *args, **options):
        max_values = Artist.objects.aggregate(
            max_spotify_followers=Max('spotify_followers'),
            max_spotify_popularity=Max('spotify_popularity'),
            max_spotify_monthly_listeners=Max('spotify_monthly_listeners'),
            max_instagram_followers=Max('instagram_followers'),
            max_tiktok_followers=Max('tiktok_followers'),
            max_tiktok_likes=Max('tiktok_likes')
        )

        # Normalize each metric and calculate weighted score
        ranked_artists = Artist.objects.annotate(
            normalized_spotify_followers=Cast('spotify_followers', FloatField()) / max_values['max_spotify_followers'],
            normalized_spotify_popularity=Cast('spotify_popularity', FloatField()) / max_values['max_spotify_popularity'],
            normalized_spotify_monthly_listeners=Cast('spotify_monthly_listeners', FloatField()) / max_values['max_spotify_monthly_listeners'],
            normalized_instagram_followers=Cast('instagram_followers', FloatField()) / max_values['max_instagram_followers'],
            normalized_tiktok_followers=Cast('tiktok_followers', FloatField()) / max_values['max_tiktok_followers'],
            normalized_tiktok_likes=Cast('tiktok_likes', FloatField()) / max_values['max_tiktok_likes']
        )

        print(ranked_artists)
        return True


