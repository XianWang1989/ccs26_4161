
from django.urls import path, include
from .views import send_message

urlpatterns = [
    path('postman/', include('postman.urls')),
    path('postman/send/', send_message, name='send_message'),
    # other paths...
]
