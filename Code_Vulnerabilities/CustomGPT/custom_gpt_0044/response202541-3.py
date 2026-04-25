
# URL that handles pages media
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", ''))
if not _media_url:
    raise ImproperlyConfigured('STATIC_URL and MEDIA_URL must be set in settings.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
