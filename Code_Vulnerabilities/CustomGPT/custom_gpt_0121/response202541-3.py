
# pages/settings.py
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", None))

if _media_url is None:
    raise ImproperlyConfigured('Neither STATIC_URL nor MEDIA_URL is set. Please check your settings.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
