
# Get the media URL, and ensure it has a valid default value if None.
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", '/static/'))
if _media_url is None:
    raise ImproperlyConfigured('Both STATIC_URL and MEDIA_URL settings are not configured.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
