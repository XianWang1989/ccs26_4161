
# settings.py

# Define the URL for serving static files
STATIC_URL = '/static/'

# Path to your static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# If you haven't already, ensure you run collectstatic
# This should be run with proper permissions
