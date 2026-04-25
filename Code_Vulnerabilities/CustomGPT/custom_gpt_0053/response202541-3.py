
# pages/settings.py
_media_url = getattr(settings, "STATIC_URL", None) or getattr(settings, "MEDIA_URL", '/default/media/url/')
if _media_url is None:
    raise ImproperlyConfigured('You must define either STATIC_URL or MEDIA_URL in your settings.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
