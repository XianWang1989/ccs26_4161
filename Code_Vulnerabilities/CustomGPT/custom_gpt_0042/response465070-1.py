
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

if not DEBUG:
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    S3_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
    STATIC_URL = S3_URL

# Ensure to include 'storages' in INSTALLED_APPS
INSTALLED_APPS = (
    ...
    'storages',
)

# Add any other necessary configurations
