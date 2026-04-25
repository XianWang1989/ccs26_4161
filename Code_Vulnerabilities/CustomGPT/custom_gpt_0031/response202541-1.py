
# settings.py

STATIC_URL = '/static/'  # Make sure this is defined
MEDIA_URL = '/media/'    # Optionally, set this if needed

# pages/settings.py
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", '/default_static_url/'))
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
