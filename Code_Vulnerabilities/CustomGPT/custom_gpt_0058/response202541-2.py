
# Ensure STATIC_URL or MEDIA_URL is set
if not getattr(settings, 'STATIC_URL', None) and not getattr(settings, 'MEDIA_URL', None):
    raise ImproperlyConfigured('Either STATIC_URL or MEDIA_URL must be defined in settings.')

# Define default STATIC_URL if not set
STATIC_URL = getattr(settings, 'STATIC_URL', '/static/')

# Define default MEDIA_URL if not set
MEDIA_URL = getattr(settings, 'MEDIA_URL', '/media/')

# Now safely create _media_url and PAGES_MEDIA_URL
_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
