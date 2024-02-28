from django.core.management.base import BaseCommand
from django.db import transaction
import csv
from artist.models import Artist
from catalog.models import Track, Genre
from django.core.files import File


class Command(BaseCommand):
    help = 'Import tracks from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to import')

    @transaction.atomic
    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']
        
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            
            for row in reader:
                artist_name = row['ARTIST NAME']
                artist, _ = Artist.objects.get_or_create(
                    name=artist_name,
                    defaults={'hometown': row['MAIN ARTIST HOMETOWN'], 'spotify_url': row['YOUR SPOTIFY ARTIST PROFILE URL']}
                )

                track, created = Track.objects.get_or_create(
                    isrc=row['SONG ISRC CODE'],
                    defaults={
                        'artist': artist,
                        'name': row['SONG NAME'],
                        'duration': int(float(row['SONG LENGTH']) * 60),  # Example conversion, adjust as needed
                        'is_cover': row['IS IT A COVER OF SOMEONE ELSE\'S SONG?'].lower() == 'yes',
                        'is_remix': row['IS IT A REMIX?'].lower() == 'yes',
                        'is_explicit': row['EXPLICIT LYRICS?'].lower() == 'yes',
                        # Add other fields as necessary
                    }
                )
                
                if created:
                    # Handle file uploads if needed, e.g.:
                    #with open(row['UPLOAD WAV FILE // MUST MATCH NAME OF SONG EXACTLY'], 'rb') as f:
                    #    track.file_wav.save(row['UPLOAD WAV FILE // MUST MATCH NAME OF SONG EXACTLY'], File(f))
                    # Repeat for other file fields
                    
                    # Add genres
                    genres = [row['GENRE 1'], row['GENRE 2'], row['GENRE 3']]
                    for genre_name in genres:
                        if genre_name:
                            genre, _ = Genre.objects.get_or_create(name=genre_name)
                            track.genres.add(genre)

                self.stdout.write(self.style.SUCCESS(f'Successfully imported "{track.name}" by {artist.name}'))
