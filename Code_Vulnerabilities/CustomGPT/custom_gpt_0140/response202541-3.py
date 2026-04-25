
# Ensure STATIC_URL and MEDIA_URL are set
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)

if _media_url is None:
    raise ImproperlyConfigured('Both STATIC_URL and MEDIA_URL must be set.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
