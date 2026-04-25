
# pages/settings.py

# Ensure that STATIC_URL and MEDIA_URL are set in your settings file
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", None))
if _media_url is None:
    raise ImproperlyConfigured('Please ensure STATIC_URL or MEDIA_URL is defined.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
