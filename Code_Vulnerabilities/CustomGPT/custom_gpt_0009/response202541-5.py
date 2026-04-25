
# Ensure STATIC_URL or MEDIA_URL are defined
_static_url = getattr(settings, "STATIC_URL", '/static/')
_media_url = _static_url  # Default to static URL if not defined

# Define PAGES_MEDIA_URL with a valid media URL base
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
