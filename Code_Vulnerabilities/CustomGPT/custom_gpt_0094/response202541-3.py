
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", '/default/static/url/'))
if _media_url is None:
    _media_url = '/default/static/url/'  # fallback URL

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
