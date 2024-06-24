release: python manage.py migrate
web: gunicorn acrylic.wsgi
worker: celery --app=acrylic worker --concurrency=2
#web: flower --app=acrylic --port=5001 --broker=$BROKER_URL --basic_auth=$FLOWER_BASIC_AUTH
