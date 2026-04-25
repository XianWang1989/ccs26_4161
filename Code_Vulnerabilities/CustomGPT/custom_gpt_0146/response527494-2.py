
from django.urls import path, include

urlpatterns = [
    ...,
    path('postman/', include('postman.urls')),  # This will include all postman URLs
]
