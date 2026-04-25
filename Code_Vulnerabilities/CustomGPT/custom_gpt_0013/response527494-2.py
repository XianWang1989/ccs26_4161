
from django.urls import path
from postman.views import send  # Import send view

urlpatterns = [
    path('send/', send, name='send_message'),
    # other URLs
]
