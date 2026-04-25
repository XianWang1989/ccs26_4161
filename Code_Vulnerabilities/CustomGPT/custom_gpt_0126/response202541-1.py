
# Ensure these settings are present in your main settings.py
STATIC_URL = '/static/'  # or your actual static URL
MEDIA_URL = '/media/'    # or your actual media URL

# Updated _media_url assignment to avoid None type
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", None))
if _media_url is None:
    raise ImproperlyConfigured('Both STATIC_URL and MEDIA_URL are not defined.')
