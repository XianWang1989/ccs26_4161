
# Ensure STATIC_URL and MEDIA_URL are set
if not hasattr(settings, 'STATIC_URL'):
    settings.STATIC_URL = '/static/'  # or your desired static URL

if not hasattr(settings, 'MEDIA_URL'):
    settings.MEDIA_URL = '/media/'  # or your desired media URL

_media_url = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
