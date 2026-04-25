
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL) or '/default/static/url/'
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
