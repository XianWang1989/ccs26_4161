
import os

# Static files (CSS, JavaScript, Images)
STATIC_URL = os.environ.get('AWS_S3_CUSTOM_DOMAIN') + '/static/'

# Configuration S3 Amazon Web Service for static serving
if not DEBUG:
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    STATICFILES_STORAGE = 'storages.backends.s3.S3Boto3Storage'
