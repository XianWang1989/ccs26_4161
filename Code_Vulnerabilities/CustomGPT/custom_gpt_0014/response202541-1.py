
# Ensure STATIC_URL and MEDIA_URL are set in your main settings.py
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", "/static/"))

# Define the default pages media URL
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))

# Check for None explicitly to raise an error if neither are set
if _media_url is None:
    raise ImproperlyConfigured('Both STATIC_URL and MEDIA_URL settings must be defined.')
