
# Modify the existing line for _media_url
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", '/default_media_url/'))
