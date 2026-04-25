
# URL that handles pages media
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)

if _media_url is None:
    raise ImproperlyConfigured('Please ensure STATIC_URL or MEDIA_URL is set.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
