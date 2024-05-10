import os
from celery import Celery
from decouple import config


#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'acrylic.settings')

app = Celery('acrylic')
#app.config_from_object('django.conf:settings', namespace='CELERY')

app.config.update(
    BROKER_URL=config('REDISCLOUD_URL', ''),
    CELERY_RESULT_BACKEND=config('REDISCLOUD_URL', '')
)

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
