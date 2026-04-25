
from django.urls import path, include

urlpatterns = [
    # other paths ...
    path('postman/', include('postman.urls')),
]
