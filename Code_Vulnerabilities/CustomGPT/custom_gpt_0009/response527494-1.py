
from django.urls import path
from postman import views as postman_views

urlpatterns = [
    path('send/', postman_views.send_message, name='send_message'),
    # ... other URL patterns
]
