import hubspot
from hubspot.crm.contacts import SimplePublicObjectInputForCreate
from hubspot.crm.contacts.exceptions import ApiException
from django.apps import apps
from django.conf import settings
from django.urls import reverse
from acrylic.celery import app


@app.task
def create_artist_in_hubspot_task(artist_id):

    if settings.HUBSPOT_ACCESS_TOKEN:
        # if the Hubspot integration is being used
        Artist = apps.get_model('artist', 'Artist')
        
        try:
            artist = Artist.objects.exclude(user=None).get(id=artist_id)
        except Artist.DoesNotExist:
            pass
        else:
            # Initialize the client
            api_client = hubspot.Client.create(access_token=settings.HUBSPOT_ACCESS_TOKEN)

            # Define the contact properties including custom fields
            contact_obj = SimplePublicObjectInputForCreate(
                properties={
                    'email': artist.user.email,
                    'firstname': artist.name,
                    'lastname': '',
                    'phone': '',
                    # custom fields
                    'uuid': str(artist.uuid),
                    'type': 'artist',
                    'admin_url': 'https://platform.acrylic.la' + reverse('admin:artist_view_object', args=[artist.id]),
                }
            )

            try:
                # Create the contact
                api_response = api_client.crm.contacts.basic_api.create(simple_public_object_input_for_create=contact_obj)
                # add hubspot_id to artist
                artist.hubspot_id = api_response.id
                artist.save()
                print("Contact created with ID:", api_response.id)
            except ApiException as e:
                print("Exception when creating contact: %s\n" % e)
    return True