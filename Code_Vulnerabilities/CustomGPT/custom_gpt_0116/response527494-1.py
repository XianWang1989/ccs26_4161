
from django.urls import path, include
from postman import views as postman_views

urlpatterns = [
    # ... other urls ...
    path('postman/', include('postman.urls')),
]
