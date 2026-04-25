
# settings.py

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Define the static files directory
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Directory where collectstatic will collect static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
