
_media_url = getattr(settings, "STATIC_URL", getattr(settings, 'MEDIA_URL', '/static/'))

if _media_url is None:
    raise ImproperlyConfigured('STATIC_URL and MEDIA_URL cannot both be None.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
