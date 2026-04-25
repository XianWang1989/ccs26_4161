
from django.urls import path
from postman import views as postman_views

urlpatterns = [
    path('send/', postman_views.send, name='postman_send'),
    path('inbox/', postman_views.inbox, name='postman_inbox'),
    # other URLs...
]
