
# Ensure MEDIA_URL or STATIC_URL are defined
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", None))
if _media_url is None:
    raise ImproperlyConfigured('Both STATIC_URL and MEDIA_URL must be set in your settings.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
