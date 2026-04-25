
# Define a default value for media URL.
DEFAULT_MEDIA_URL = '/static/'  # or any default you see fit

# Get the media URL or fallback to the default
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", DEFAULT_MEDIA_URL))

# Now set PAGES_MEDIA_URL
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
