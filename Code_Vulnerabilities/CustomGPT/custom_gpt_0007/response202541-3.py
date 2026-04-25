
# Add this in your settings.py or ensure similar lines exist
STATIC_URL = '/static/'  # Define your static URL if not defined
MEDIA_URL = '/media/'  # Define your media URL if not defined

# Update _media_url definition
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL or '/media/')
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
