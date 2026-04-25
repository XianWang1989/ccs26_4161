
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)

# Ensure _media_url is set; raise an error if not
if not _media_url:
    raise ImproperlyConfigured("STATIC_URL or MEDIA_URL must be set.")

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
