
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", "/default/media/url/"))  # Provide a default URL if both are None
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
