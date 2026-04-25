
import os

# AWS S3 Configuration
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
STATIC_URL = S3_URL

# Media configuration
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'  # Adjust if required
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
