
from django.urls import path
from postman import views as postman_views

urlpatterns = [
    path('inbox/', postman_views.inbox, name='inbox'),
    path('send/', postman_views.send, name='send'),
    # Add other necessary paths...
]
