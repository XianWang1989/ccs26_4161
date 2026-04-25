
# settings.py
import os

DEBUG = False

ALLOWED_HOSTS = ['my_server_ip', 'localhost']

# Static files settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Other settings...
