
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", ''))
if not _media_url:
    raise ImproperlyConfigured('Both STATIC_URL and MEDIA_URL are not set.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
