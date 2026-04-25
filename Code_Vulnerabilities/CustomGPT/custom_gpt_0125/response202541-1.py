
# settings.py

# Ensure these are set to valid URLs
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Set up the _media_url
_media_url = getattr(settings, "STATIC_URL", MEDIA_URL)

# Continue with the rest of your settings code...
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
