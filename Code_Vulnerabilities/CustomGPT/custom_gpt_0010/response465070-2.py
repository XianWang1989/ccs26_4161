
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# AWS S3 settings
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = f'http://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'
STATIC_URL = S3_URL
