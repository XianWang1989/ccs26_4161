
_media_url = getattr(settings, "STATIC_URL", "/static/")
if _media_url is None:
    _media_url = "/media/"
