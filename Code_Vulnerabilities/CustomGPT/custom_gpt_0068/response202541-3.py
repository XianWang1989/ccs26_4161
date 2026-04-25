
# settings.py
# Ensure that these settings are defined
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Existing settings
try:
    _media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
except AttributeError:
    _media_url = None

if _media_url is None:
    raise ImproperlyConfigured('Either STATIC_URL or MEDIA_URL must be defined in the settings.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
