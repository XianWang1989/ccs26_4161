
# Assuming you have STATIC_URL or MEDIA_URL set
_media_url = getattr(settings, "STATIC_URL", getattr(settings, "MEDIA_URL", '/default/static/'))

# Join to create pages media URL
PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
