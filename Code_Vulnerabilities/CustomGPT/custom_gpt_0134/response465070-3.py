
import os

# AWS S3 settings
if not DEBUG:
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', 'your_bucket_name')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', 'your_access_key_id')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', 'your_secret_access_key')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    S3_URL = f'http://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'
    STATIC_URL = S3_URL
