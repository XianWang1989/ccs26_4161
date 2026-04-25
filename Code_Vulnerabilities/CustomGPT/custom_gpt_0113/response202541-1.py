
# Assuming STATIC_URL is usually used for serving static files
_static_url = getattr(settings, "STATIC_URL", "/static/")  # Default to '/static/' if not set
_media_url = getattr(settings, "MEDIA_URL", "/media/")  # Default to '/media/' if not set

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
