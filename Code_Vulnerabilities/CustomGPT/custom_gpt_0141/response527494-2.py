
from django.conf.urls import url, include

urlpatterns = [
    ...,
    url(r'^postman/', include('postman.urls', namespace='postman')),
]
