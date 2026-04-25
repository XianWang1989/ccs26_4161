
# Default settings
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Media URL handling in pages/settings.py
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", '/default/static/'))
if _media_url is None or _media_url == '':
    raise ImproperlyConfigured('Both STATIC_URL and MEDIA_URL are not defined.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
