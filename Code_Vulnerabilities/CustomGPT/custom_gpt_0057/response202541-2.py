
# Add these lines to your settings.py
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Ensure PAGE_MEDIA_URL is set correctly
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
