
_media_url = getattr(settings, "STATIC_URL", None) or getattr(settings, "MEDIA_URL", '/static/')
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/') if _media_url else '/static/pages/')
