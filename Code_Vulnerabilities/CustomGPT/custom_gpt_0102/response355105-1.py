
# settings.py

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Activate collection of static files
if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'your_app/static'),
    ]
