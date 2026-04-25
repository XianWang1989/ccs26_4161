
# pages/settings.py

# Ensure these variables are defined in your main settings.py
STATIC_URL = getattr(settings, "STATIC_URL", None)
MEDIA_URL = getattr(settings, "MEDIA_URL", None)

# Check if at least one of these is defined
if not STATIC_URL and not MEDIA_URL:
    raise ImproperlyConfigured("Please define either STATIC_URL or MEDIA_URL in your settings.")

# Use MEDIA_URL if STATIC_URL is not defined
_media_url = STATIC_URL or MEDIA_URL

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
