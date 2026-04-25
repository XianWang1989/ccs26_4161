
from django.urls import path, include

urlpatterns = [
    # Other URL patterns
    path('postman/', include('postman.urls')),
]
