
from django.urls import path
from postman import views as postman_views

urlpatterns = [
    path('postman/send/', postman_views.send_message, name='send_message'),
    path('postman/inbox/', postman_views.inbox, name='inbox'),
    # Other URLs...
]
