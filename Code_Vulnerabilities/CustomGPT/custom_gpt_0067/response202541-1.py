
# settings.py

# Ensure STATIC_URL and MEDIA_URL are defined
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Your existing code
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
