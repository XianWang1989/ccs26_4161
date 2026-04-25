
# pages/settings.py

# Ensure that STATIC_URL or MEDIA_URL is set
STATIC_URL = getattr(settings, 'STATIC_URL', '/static/')
MEDIA_URL = getattr(settings, 'MEDIA_URL', '/media/')

_media_url = STATIC_URL  # Use STATIC_URL by default
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
