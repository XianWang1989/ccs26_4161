
from django.urls import path, include

urlpatterns = [
    ...
    path('postman/', include('postman.urls')),  # Include the Postman URLs
]
