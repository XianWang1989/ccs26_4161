
# Inside your pages/settings.py
from django.core.exceptions import ImproperlyConfigured

_media_url = getattr(settings, "STATIC_URL", None) or getattr(settings, "MEDIA_URL", None)

if _media_url is None:
    raise ImproperlyConfigured('Please ensure STATIC_URL or MEDIA_URL is set in your settings.')
