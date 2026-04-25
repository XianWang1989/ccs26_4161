
from django.urls import path
from postman import views as postman_views

urlpatterns = [
    path('messages/send/', postman_views.send_message, name='send_message'),
    path('inbox/', postman_views.inbox, name='inbox'),
    # other URLs...
]
