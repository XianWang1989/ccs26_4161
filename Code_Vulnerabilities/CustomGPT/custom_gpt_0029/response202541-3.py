
from os.path import join
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# Ensure STATIC_URL and MEDIA_URL are set
STATIC_URL = getattr(settings, 'STATIC_URL', '/static/')
MEDIA_URL = getattr(settings, 'MEDIA_URL', '/media/')

_media_url = STATIC_URL if STATIC_URL else MEDIA_URL
if _media_url is None:
    raise ImproperlyConfigured("Both STATIC_URL and MEDIA_URL should be defined.")

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
