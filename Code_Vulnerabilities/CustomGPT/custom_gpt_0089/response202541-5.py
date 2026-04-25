
# Default media URL handling
_media_url = getattr(settings, "STATIC_URL", getattr(settings, 'MEDIA_URL', '/media/'))  # Default fallback
if _media_url is None:
    _media_url = '/media/'  # Ensure it's not None

PAGES_MEDIA_URL = join(_media_url, 'pages/')
