
# Ensure _media_url has a default if both STATIC_URL and MEDIA_URL are not set
_static_url = getattr(settings, "STATIC_URL", None)
_media_url = getattr(settings, "MEDIA_URL", "/static/")  # Default to '/static/' if none

# If _static_url is not set, use _media_url instead
if _static_url is None and _media_url is None:
    raise ImproperlyConfigured('Neither STATIC_URL nor MEDIA_URL is set.')

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_static_url or _media_url, 'pages/'))
