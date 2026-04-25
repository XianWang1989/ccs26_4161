
from django.urls import path, include

urlpatterns = [
    # other URLs
    path('postman/', include('postman.urls')),
]
