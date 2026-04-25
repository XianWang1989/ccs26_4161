
from os.path import join
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# Check for STATIC_URL and MEDIA_URL
STATIC_URL = getattr(settings, "STATIC_URL", None)
MEDIA_URL = getattr(settings, "MEDIA_URL", None)

if STATIC_URL is None and MEDIA_URL is None:
    raise ImproperlyConfigured("You must define STATIC_URL or MEDIA_URL in your settings.")

_media_url = STATIC_URL or MEDIA_URL  # Fallback to MEDIA_URL if STATIC_URL is not set

PAGES_MEDIA_URL = join(_media_url, 'pages/')
