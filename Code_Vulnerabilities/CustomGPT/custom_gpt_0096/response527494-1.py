
from django.urls import path
from postman.views import send

urlpatterns = [
    path('send/', send, name='postman:send'),
]
