
# settings.py

# Ensure these URLs are defined
STATIC_URL = '/static/'  # Update as necessary for your project
MEDIA_URL = '/media/'    # Update as necessary for your project

# Existing setting code
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
