
# settings.py

# Ensure these URLs are defined
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Alternatively, one of these needs to be set if you want to use it in pages/settings.py
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
