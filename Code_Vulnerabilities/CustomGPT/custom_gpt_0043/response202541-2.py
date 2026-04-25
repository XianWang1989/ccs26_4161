
# URL that handles pages media
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)

# Check if _media_url is None or an empty string and assign a default value if so
if not _media_url:
    _media_url = '/static/'  # Default value or adjust according to your project's setup

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
