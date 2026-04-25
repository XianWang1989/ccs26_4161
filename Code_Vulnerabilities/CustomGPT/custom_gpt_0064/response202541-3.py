
from os.path import join
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# Ensure required settings are present
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", None))
if _media_url is None:
    raise ImproperlyConfigured('Please make sure both STATIC_URL and MEDIA_URL are defined.')

# Define your media URL
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
