
from django.urls import path, include

urlpatterns = [
    # ... other url patterns
    path('postman/', include('postman.urls')),
]
