
# settings.py

# Define STATIC_URL for serving static files
STATIC_URL = '/static/'

# Define MEDIA_URL for serving user-uploaded files
MEDIA_URL = '/media/'

# Add the following line in pages/settings.py if _media_url isn't set
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
if _media_url is None:
    raise ImproperlyConfigured('Please make sure you specified STATIC_URL or MEDIA_URL setting.')
