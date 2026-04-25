
# pages/settings.py
from os.path import join
from django.conf import settings

# Default settings in case STATIC_URL or MEDIA_URL are not set
DEFAULT_STATIC_URL = '/static/'
DEFAULT_MEDIA_URL = '/media/'

_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", DEFAULT_STATIC_URL))
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
