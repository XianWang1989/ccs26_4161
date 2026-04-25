
# settings.py

# Ensure these variables are set
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Now, your pages/settings.py should work correctly
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
