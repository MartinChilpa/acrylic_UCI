web: gunicorn acrylic.wsgi
worker: celery --app=acrylic worker --concurrency=2
flower: celery --app=acrylic flower --port=5001  --basic-auth=acrylic:zenx