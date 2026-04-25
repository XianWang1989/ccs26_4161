
# Ensure STATIC_URL or MEDIA_URL is set
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", '/static/'))
if _media_url is None:
    raise ImproperlyConfigured('Either STATIC_URL or MEDIA_URL must be set in settings.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
