
# URL that handles pages media and uses <MEDIA_ROOT>/pages by default.
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", "/static/"))

# Ensure that _media_url is set to a default if both STATIC_URL and MEDIA_URL are missing
if _media_url is None:
    raise ImproperlyConfigured("STATIC_URL or MEDIA_URL must be defined in the settings.")

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
