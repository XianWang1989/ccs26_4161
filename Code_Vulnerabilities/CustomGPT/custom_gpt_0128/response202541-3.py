
# In your settings.py
STATIC_URL = '/static/'  # Define the static URL
MEDIA_URL = '/media/'    # Define the media URL

# Your existing settings
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
