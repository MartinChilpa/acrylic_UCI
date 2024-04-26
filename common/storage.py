from django.conf import settings
from storages.backends.s3 import S3Storage


# public access S3 bucket
public_storage = S3Storage(bucket_name=settings.PUBLIC_S3_BUCKET)
