
from django.urls import include, path

urlpatterns = [
    path('postman/', include('postman.urls')),
    # other paths...
]
