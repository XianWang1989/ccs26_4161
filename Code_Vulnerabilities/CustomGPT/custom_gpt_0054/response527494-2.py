
from django.urls import path, include

urlpatterns = [
    # Other paths...
    path('postman/', include('postman.urls')),
]
