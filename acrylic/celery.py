import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'acrylic.settings')

app = Celery('acrylic')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update(
    BROKER_URL=os.environ['REDISCLOUD_URL'],
    CELERY_RESULT_BACKEND=os.environ['REDISCLOUD_URL']
)

app.autodiscover_tasks()
