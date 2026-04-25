
# Make sure to define STATIC_URL or MEDIA_URL in your settings.py
if not getattr(settings, "STATIC_URL", None) and not getattr(settings, "MEDIA_URL", None):
    raise ImproperlyConfigured('You must define STATIC_URL or MEDIA_URL in your settings.')

_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
