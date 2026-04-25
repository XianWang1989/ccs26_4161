
import os

# AWS S3 Configuration
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', 'your-bucket-name')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', 'your-access-key')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', 'your-secret-key')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'

# Don't forget to set these in Heroku
# heroku config:set AWS_STORAGE_BUCKET_NAME='your-bucket-name'
# heroku config:set AWS_ACCESS_KEY_ID='your-access-key'
# heroku config:set AWS_SECRET_ACCESS_KEY='your-secret-key'
