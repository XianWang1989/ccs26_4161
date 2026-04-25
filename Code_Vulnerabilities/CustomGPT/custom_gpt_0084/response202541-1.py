
# Ensure STATIC_URL and MEDIA_URL are defined
if not getattr(settings, 'STATIC_URL', None):
    raise ImproperlyConfigured('STATIC_URL must be set in settings.')

if not getattr(settings, 'MEDIA_URL', None):
    raise ImproperlyConfigured('MEDIA_URL must be set in settings.')

_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
