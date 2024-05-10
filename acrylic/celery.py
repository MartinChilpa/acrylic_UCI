import os
from celery import Celery
from decouple import config


#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'acrylic.settings')

app = Celery('acrylic')
#app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
    BROKER_URL=config('REDIS_URL', ''),
    CELERY_RESULT_BACKEND=config('REDIS_URL', '')
)

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
