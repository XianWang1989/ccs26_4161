
from os.path import join
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# Ensure default settings are defined
_media_url = getattr(settings, "STATIC_URL", getattr(settings, 'MEDIA_URL', '/default/media/path/'))

# URL setup for pages media
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))

# Rest of your settings...
