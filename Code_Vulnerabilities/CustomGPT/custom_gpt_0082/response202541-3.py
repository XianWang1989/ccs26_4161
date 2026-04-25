
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", '/default/url/'))
if _media_url is None:
    raise ImproperlyConfigured('Both STATIC_URL and MEDIA_URL are not set.')
