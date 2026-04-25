
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# AWS S3 Configuration
if not DEBUG:
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    S3_URL = f"http://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/"
    STATIC_URL = S3_URL
