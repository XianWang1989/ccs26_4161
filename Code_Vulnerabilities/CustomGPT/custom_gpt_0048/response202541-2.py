
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)

# Check for None values and set a default if necessary
if _media_url is None:
    raise ImproperlyConfigured('STATIC_URL or MEDIA_URL must be set.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
