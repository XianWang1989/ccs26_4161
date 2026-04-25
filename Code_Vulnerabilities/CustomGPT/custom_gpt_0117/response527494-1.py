
from django.urls import path
from postman import views as postman_views

urlpatterns = [
    path('send/', postman_views.send, name='postman_send'),
    # Other URLs...
]
