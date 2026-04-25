
# Enhanced media URL configuration in pages/settings.py
from django.core.exceptions import ImproperlyConfigured

_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", None))

if _media_url is None:
    raise ImproperlyConfigured('Please ensure STATIC_URL or MEDIA_URL is set in your settings.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
