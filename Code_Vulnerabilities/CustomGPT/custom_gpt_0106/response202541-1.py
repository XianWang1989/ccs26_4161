
# URL that handles pages media and uses <MEDIA_ROOT>/pages by default.
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", '/static/'))

# Ensure _media_url is not None
if _media_url is None:
    _media_url = '/static/'  # Default to a sensible static URL
