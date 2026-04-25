
# urls.py
from django.urls import include, path

urlpatterns = [
    ...
    path('postman/', include('postman.urls', namespace='postman')),
    ...
]
