
# Ensure STATIC_URL or MEDIA_URL is set
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL or '/static/')

if _media_url is None:
    raise ImproperlyConfigured('Both STATIC_URL and MEDIA_URL cannot be None.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
