
from os.path import join
from django.conf import settings

# Set default for STATIC_URL and MEDIA_URL if not defined
_media_url = getattr(settings, "STATIC_URL", "/static/")
if _media_url is None:
    _media_url = "/media/"

PAGES_MEDIA_URL = getattr(settings, 'PAGES_MEDIA_URL', join(_media_url, 'pages/'))
