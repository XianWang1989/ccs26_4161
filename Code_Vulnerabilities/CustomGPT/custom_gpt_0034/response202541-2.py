
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
if _media_url is None:
    raise ImproperlyConfigured("STATIC_URL must not be None.")
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL',
    join(_media_url, 'pages/'))
