
_media_url = getattr(settings, "STATIC_URL", None) or getattr(settings, "MEDIA_URL", None)

if not _media_url:
    raise ImproperlyConfigured('Please specify a STATIC_URL or MEDIA_URL in your settings.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
