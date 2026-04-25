
from django.urls import include, path

urlpatterns = [
    ...
    path('messages/', include('postman.urls')),
]
