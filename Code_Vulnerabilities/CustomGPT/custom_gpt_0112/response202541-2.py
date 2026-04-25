
_media_url = getattr(settings, "STATIC_URL", None) or getattr(settings, "MEDIA_URL", None)
if _media_url is None:
    raise ImproperlyConfigured('Both STATIC_URL and MEDIA_URL are not set. Please configure at least one of them.')
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
