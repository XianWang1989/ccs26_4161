
# Ensure these settings are defined in your main settings module
STATIC_URL = getattr(settings, 'STATIC_URL', '/static/')
MEDIA_URL = getattr(settings, 'MEDIA_URL', '/media/')

# Then, make sure _media_url gets a valid value
_media_url = getattr(settings, "STATIC_URL", MEDIA_URL)
if _media_url is None:
    raise ImproperlyConfigured("STATIC_URL or MEDIA_URL must be set.")

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
