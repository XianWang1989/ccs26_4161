
# Define _media_url with a fallback
_media_url = getattr(settings, "STATIC_URL", getattr(settings, 'MEDIA_URL', '/static/'))

# Raise an error if _media_url is still None
if _media_url is None:
    raise ImproperlyConfigured('Both STATIC_URL and MEDIA_URL must be defined.')

# Now safely set PAGES_MEDIA_URL
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
