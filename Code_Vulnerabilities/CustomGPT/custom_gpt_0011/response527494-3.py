
from django.urls import path
from .views import send_message

urlpatterns = [
    # other paths ...
    path('send/', send_message, name='send_message'),
]
