
# Ensure STATIC_URL and MEDIA_URL are set
STATIC_URL = getattr(settings, 'STATIC_URL', '/static/')
MEDIA_URL = getattr(settings, 'MEDIA_URL', '/media/')

_media_url = getattr(settings, "STATIC_URL", None) or getattr(settings, "MEDIA_URL", None)
if _media_url is None:
    raise ImproperlyConfigured('Please make sure you specify either STATIC_URL or MEDIA_URL.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
