from django.apps import apps
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


# Django auth base user extension        
User = get_user_model()

# add type field
#User.add_to_class('type', models.CharField(max_length=10, choices=UserType.choices, blank=True, null=True))


# add get_profile() method
@property
def get_profile(self):
      """  user.artist / user.buyer """
      artist = getattr(user, 'artist', None)
      if artist:
            return artist
      return getattr(user, 'buyer', None)
User.add_to_class('profile', get_profile)


#class Biiilng
#    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name))