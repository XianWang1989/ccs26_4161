
# settings.py

_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)

if _media_url is None:
    raise ImproperlyConfigured('Both STATIC_URL and MEDIA_URL are not defined in your settings.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
