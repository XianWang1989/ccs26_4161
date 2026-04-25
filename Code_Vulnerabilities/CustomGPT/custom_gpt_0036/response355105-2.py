
import os

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # or wherever your static files are collected

# Ensure you run this command as www-data after you modify STATIC_ROOT
# python manage.py collectstatic
