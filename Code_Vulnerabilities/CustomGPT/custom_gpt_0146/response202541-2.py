
# pages/settings.py

from django.conf import settings

# Check if STATIC_URL or MEDIA_URL is None and assign a default if necessary
_media_url = getattr(settings, "STATIC_URL", None) or getattr(settings, "MEDIA_URL", '/default/media/')
