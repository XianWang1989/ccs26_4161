
from django.urls import path, include

urlpatterns = [
    # Your other URL patterns
    path('postman/', include('postman.urls')),
]
