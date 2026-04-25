
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", None))

# Ensure _media_url is a string before joining
if _media_url is None:
    raise ImproperlyConfigured("Please ensure STATIC_URL or MEDIA_URL is set in your Django settings.")

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
