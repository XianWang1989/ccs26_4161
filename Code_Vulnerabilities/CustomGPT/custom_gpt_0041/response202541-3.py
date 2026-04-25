
if _media_url is None:
    raise ImproperlyConfigured("Please ensure STATIC_URL or MEDIA_URL is set.")
PAGES_MEDIA_URL = join(_media_url, 'pages/')
