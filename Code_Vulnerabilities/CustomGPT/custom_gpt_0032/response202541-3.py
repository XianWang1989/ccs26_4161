
# Ensure STATIC_URL and MEDIA_URL are set
_media_url = getattr(settings, "STATIC_URL", None)
if _media_url is None:
    raise ImproperlyConfigured('STATIC_URL must be set.')

# Check if MEDIA_URL is defined as a fallback
if settings.MEDIA_URL is not None:
    _media_url = settings.MEDIA_URL

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
