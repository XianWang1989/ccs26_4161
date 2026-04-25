
# In your settings.py file

# Ensure STATIC_URL and MEDIA_URL are set correctly
# These settings specify the base URL for static and media files
STATIC_URL = '/static/'  # Make sure you have this set
MEDIA_URL = '/media/'    # Make sure you have this set

# Now, when you get _media_url, it will never be None
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)

# PAGES_MEDIA_URL should now work as expected
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL',
    join(_media_url, 'pages/'))
