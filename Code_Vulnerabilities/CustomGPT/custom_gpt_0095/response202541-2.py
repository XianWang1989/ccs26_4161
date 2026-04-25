
# Ensure STATIC_URL and MEDIA_URL are set
STATIC_URL = getattr(settings, 'STATIC_URL', '/static/')
MEDIA_URL = getattr(settings, 'MEDIA_URL', '/media/')

_media_url = getattr(settings, "STATIC_URL", STATIC_URL)  # Ensure _media_url has a valid value
if _media_url is None:
    raise ImproperlyConfigured('STATIC_URL or MEDIA_URL must be defined.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL',
    join(_media_url, 'pages/'))
