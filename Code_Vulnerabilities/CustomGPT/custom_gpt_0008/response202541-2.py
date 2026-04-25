
# Get media url, ensuring it is not None
_media_url = getattr(settings, "STATIC_URL", getattr(settings, 'MEDIA_URL', None))

# Raise an exception if both are None
if _media_url is None:
    raise ImproperlyConfigured('Please specify either STATIC_URL or MEDIA_URL in your settings.')

# Define pages media URL
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
