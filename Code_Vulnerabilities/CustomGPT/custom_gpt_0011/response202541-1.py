
# URL that handles pages media and uses <MEDIA_ROOT>/pages by default.
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)

# Check if _media_url is valid. If not, raise an error.
if _media_url is None:
    raise ImproperlyConfigured('STATIC_URL and MEDIA_URL settings must be defined.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
