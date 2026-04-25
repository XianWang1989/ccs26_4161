
# Add the following lines in your settings.py
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Ensure default settings for pages application
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
