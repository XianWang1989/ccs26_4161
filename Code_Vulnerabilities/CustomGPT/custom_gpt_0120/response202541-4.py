
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", '/default/static/'))
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
