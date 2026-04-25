
# Fetch STATIC_URL and MEDIA_URL safely
STATIC_URL = getattr(settings, "STATIC_URL", None)
MEDIA_URL = getattr(settings, "MEDIA_URL", None)

if not STATIC_URL and not MEDIA_URL:
    raise ImproperlyConfigured("You must define either STATIC_URL or MEDIA_URL in your settings.")

_media_url = STATIC_URL or MEDIA_URL  # Use STATIC_URL if available, otherwise use MEDIA_URL
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
