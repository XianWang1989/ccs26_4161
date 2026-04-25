
# settings.py

# Make sure to set STATIC_URL or MEDIA_URL
STATIC_URL = getattr(settings, 'STATIC_URL', '/static/')
MEDIA_URL = getattr(settings, 'MEDIA_URL', '/media/')

# Ensure that at least one URL is available for joining paths later
if not STATIC_URL and not MEDIA_URL:
    raise ImproperlyConfigured('Either STATIC_URL or MEDIA_URL must be set.')

# Assign _media_url based on the defined STATIC_URL or MEDIA_URL
_media_url = STATIC_URL if STATIC_URL else MEDIA_URL

# Make sure to have PAGES_MEDIA_URL derived from _media_url
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
