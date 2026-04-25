
from django.conf.urls import url
from tastypie.api import Api
from .resources import GalleryResource, ImageResource

api = Api(api_name='v1')
api.register(GalleryResource())
api.register(ImageResource())

urlpatterns = [
    url(r'^api/', include(api.urls)),
]
