
# Configuration S3 for static serving
if not DEBUG:
    AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
    AWS_ACCESS_KEY_ID = 'your-access-key-id'  # Update this line
    AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'  # Update this line
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = S3_URL
