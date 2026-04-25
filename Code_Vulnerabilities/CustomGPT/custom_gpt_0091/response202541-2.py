
# Ensure STATIC_URL or MEDIA_URL is set and handle None case
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", '/static/'))
if _media_url is None:
    raise ImproperlyConfigured("Both STATIC_URL and MEDIA_URL settings must be defined.")

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
