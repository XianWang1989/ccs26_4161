
from django.urls import path, include

urlpatterns = [
    # other urls...
    path('postman/', include('postman.urls')),
]
