
import os
import dj_database_url

# AWS settings
AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# Static files settings
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Ensure you have debugging turned off in production
DEBUG = False

# Heroku settings for database
DATABASES = {'default': dj_database_url.config()}

# Allow all hosts (adjust in production settings)
ALLOWED_HOSTS = ['*']
