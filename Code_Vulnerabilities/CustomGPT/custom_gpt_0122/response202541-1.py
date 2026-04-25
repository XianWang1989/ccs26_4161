
# URL that handles pages media and uses <MEDIA_ROOT>/pages by default.
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", "/static/"))  # Default to '/static/'

if _media_url is None:
    raise ImproperlyConfigured('Both STATIC_URL and MEDIA_URL are not set in settings.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
