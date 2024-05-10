import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'acrylic.settings')

app = Celery('acrylic')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
