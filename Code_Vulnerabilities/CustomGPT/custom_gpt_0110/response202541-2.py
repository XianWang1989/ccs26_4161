
# Ensure STATIC_URL is defined
if not getattr(settings, "STATIC_URL", None) and not getattr(settings, "MEDIA_URL", None):
    raise ImproperlyConfigured('Either STATIC_URL or MEDIA_URL must be defined.')

_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
