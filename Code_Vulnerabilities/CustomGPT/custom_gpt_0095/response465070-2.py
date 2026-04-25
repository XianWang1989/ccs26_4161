
import os

# AWS S3 Storage Configuration
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

# Custom domain for S3 Bucket
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# Set static files storage
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'
STATIC_URL = S3_URL
