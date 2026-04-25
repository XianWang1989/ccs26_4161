
# URL that handles pages media and uses <MEDIA_ROOT>/pages by default.
_media_url = getattr(settings, "STATIC_URL", getattr(settings, 'MEDIA_URL', '/static/'))  # Default to '/static/' if both are None
if _media_url is None:
    raise ImproperlyConfigured("Either 'STATIC_URL' or 'MEDIA_URL' must be set.")

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
