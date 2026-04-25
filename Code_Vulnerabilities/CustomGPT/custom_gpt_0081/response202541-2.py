
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", '/default/path/'))

# Ensure _media_url is not None
if _media_url is None:
    raise ImproperlyConfigured("Both STATIC_URL and MEDIA_URL cannot be None.")

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
