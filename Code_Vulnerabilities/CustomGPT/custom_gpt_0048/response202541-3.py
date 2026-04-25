
# Ensure STATIC_URL and MEDIA_URL are defined in your settings
STATIC_URL = '/static/'  # Your static URL
MEDIA_URL = '/media/'    # Your media URL

_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)

# Raise an exception if both are none to prevent NoneType errors
if _media_url is None:
    raise ImproperlyConfigured('STATIC_URL or MEDIA_URL must be set.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
