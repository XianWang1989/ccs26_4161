
# Ensure _media_url has a default if not set
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", '/default/static/'))

# Then safely join it
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
