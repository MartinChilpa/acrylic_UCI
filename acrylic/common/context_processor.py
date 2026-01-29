from django.conf import settings


def django_settings(request):
    # Define the settings you want to expose
    return {
        'settings': settings
    }
