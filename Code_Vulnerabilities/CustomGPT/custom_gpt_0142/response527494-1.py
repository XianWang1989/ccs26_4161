
from django.urls import path
from postman import views as postman_views

urlpatterns = [
    path('post/send/', postman_views.sendMessage, name='post_message'),
    # Add other paths as required
]
