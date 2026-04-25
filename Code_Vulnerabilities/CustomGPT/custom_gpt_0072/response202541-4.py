
# settings.py
# Ensure these lines are present
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Your existing settings...
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
