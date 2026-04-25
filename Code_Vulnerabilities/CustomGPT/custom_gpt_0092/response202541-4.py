
# pages/settings.py

from os.path import join
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# Ensure STATIC_URL and MEDIA_URL are configured
STATIC_URL = getattr(settings, 'STATIC_URL', '/static/')
MEDIA_URL = getattr(settings, 'MEDIA_URL', '/media/')

# Use a fallback to prevent NoneType errors
_media_url = STATIC_URL if STATIC_URL else "/default/static/path/"
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))

# Confirm if PAGES_MEDIA_URL is correctly formed
if not isinstance(PAGES_MEDIA_URL, str):
    raise ImproperlyConfigured('PAGES_MEDIA_URL must be a valid string path.')
