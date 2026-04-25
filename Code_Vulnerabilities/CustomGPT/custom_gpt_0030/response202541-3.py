
# Get STATIC_URL or MEDIA_URL, with a fallback to a default value
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", '/media/'))

# Check for valid URLs
if _media_url is None:
    raise ImproperlyConfigured('STATIC_URL and MEDIA_URL must be set in settings.')

# Construct PAGES_MEDIA_URL
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
