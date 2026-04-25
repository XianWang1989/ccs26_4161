
# Ensure that STATIC_URL or MEDIA_URL is properly set in your Django settings
_media_url = getattr(settings, "STATIC_URL", getattr(settings, 'MEDIA_URL', '/default/media/path/'))

# After this line, you can now safely join the URL
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
