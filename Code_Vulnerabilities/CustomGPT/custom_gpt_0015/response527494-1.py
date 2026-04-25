
from django.urls import path, include

urlpatterns = [
    path('postman/', include('postman.urls')),
    # ... other urls
]
