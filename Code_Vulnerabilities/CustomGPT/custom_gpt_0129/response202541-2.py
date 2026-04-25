
# pages/settings.py
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
if _media_url is None:
    raise ImproperlyConfigured('Please make sure you have defined STATIC_URL or MEDIA_URL.')
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
