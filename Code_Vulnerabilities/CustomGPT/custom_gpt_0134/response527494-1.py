
from django.urls import path, include

urlpatterns = [
    path('postman/', include('postman.urls', namespace='postman')),
    # other url patterns...
]
