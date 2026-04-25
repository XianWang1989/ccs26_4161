
# Ensuring a fallback for _media_url
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", '/static/'))
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
