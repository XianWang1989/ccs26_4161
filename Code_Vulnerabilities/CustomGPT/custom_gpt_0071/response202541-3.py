
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)

if not _media_url:  # Check if _media_url is None or empty
    raise ImproperlyConfigured('STATIC_URL or MEDIA_URL must be defined in settings.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
