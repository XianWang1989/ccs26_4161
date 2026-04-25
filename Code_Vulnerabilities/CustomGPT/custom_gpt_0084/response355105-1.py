
# settings.py

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Ensure you have this middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Other middleware...
]

# Collect static files at deployment
# Run this command: python manage.py collectstatic
