
# Ensure these settings are defined
STATIC_URL = '/static/'  # Adjust to your static file path
MEDIA_URL = '/media/'    # Adjust to your media file path

# Use STATIC_URL or MEDIA_URL for _media_url
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)

# Ensure _media_url is properly set
if _media_url is None:
    raise ImproperlyConfigured('Both STATIC_URL and MEDIA_URL are not set.')
