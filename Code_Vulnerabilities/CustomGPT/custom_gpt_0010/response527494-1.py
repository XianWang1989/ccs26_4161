
from django.urls import path
from postman import views as postman_views

urlpatterns = [
    path('inbox/', postman_views.inbox, name='inbox'),
    path('send/', postman_views.send_message, name='send_message'),  # Ensure this is defined
]
