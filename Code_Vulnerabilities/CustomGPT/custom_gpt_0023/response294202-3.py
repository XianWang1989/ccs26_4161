
from django.conf.urls import url, include
from tastypie.api import Api
from gallery_app.resources import GalleryResource, ImageResource

v1_api = Api(api_name='v1')
v1_api.register(GalleryResource())
v1_api.register(ImageResource())

urlpatterns = [
    url(r'^api/', include(v1_api.urls)),
    # your other urlpatterns
]
