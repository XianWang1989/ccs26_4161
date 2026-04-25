
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", None))

# Check if _media_url is None and raise an appropriate error
if _media_url is None:
    raise ImproperlyConfigured('Either STATIC_URL or MEDIA_URL must be set')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
