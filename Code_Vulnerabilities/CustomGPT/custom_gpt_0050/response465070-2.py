
import os

# AWS S3 Configuration
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# Custom domain
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# Storage configurations
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'
STATIC_URL = S3_URL
