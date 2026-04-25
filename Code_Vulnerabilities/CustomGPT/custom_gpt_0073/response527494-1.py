
from django.urls import path, include

urlpatterns = [
    # Other URLs
    path('postman/', include('postman.urls', namespace='postman')),
]
