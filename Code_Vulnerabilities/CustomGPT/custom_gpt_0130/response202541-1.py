
# settings.py

# Ensure these values are set
STATIC_URL = '/static/'  # or your desired static URL path
MEDIA_URL = '/media/'    # or your desired media URL path

# Your existing code
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
