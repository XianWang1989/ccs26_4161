
# pages/settings.py

_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
if _media_url is None:
    _media_url = '/static/'  # Default fallback URL

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
