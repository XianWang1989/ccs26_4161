
# URL that handles pages media and uses <MEDIA_ROOT>/pages by default.
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)

# Check if _media_url is None and assign an appropriate default
if _media_url is None:
    raise ImproperlyConfigured('Please make sure STATIC_URL or MEDIA_URL '
                               'is set in your project settings.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL',
    join(_media_url, 'pages/'))
