
# settings.py

# Static and media URLs
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Additional pages configuration
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
