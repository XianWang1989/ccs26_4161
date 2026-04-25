
# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Command to collect static files
# Run this in your terminal
python manage.py collectstatic
