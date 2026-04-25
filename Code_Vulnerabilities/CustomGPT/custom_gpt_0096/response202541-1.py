
# URL that handles pages media and uses <MEDIA_ROOT>/pages by default.
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)

# Add a check to ensure _media_url is not None
if _media_url is None:
    raise ImproperlyConfigured('Please set STATIC_URL or MEDIA_URL in your settings.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
