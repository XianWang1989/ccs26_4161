
# Ensure static URL and media URL are valid, default to empty string
_media_url = getattr(settings, "STATIC_URL", '/static/') or ''
if not _media_url:
    raise ImproperlyConfigured('STATIC_URL is not set correctly.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
