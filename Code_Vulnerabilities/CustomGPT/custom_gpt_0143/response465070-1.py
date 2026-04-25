
if not DEBUG:
    AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
    AWS_ACCESS_KEY_ID = 'your-access-key'
    AWS_SECRET_ACCESS_KEY = 'your-secret-key'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATIC_URL = f'http://{AWS_S3_CUSTOM_DOMAIN}/'
