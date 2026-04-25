
from django.urls import path
from postman import views as postman_views

urlpatterns = [
    path('postman/send/', postman_views.send, name='send_message'),
    # ... other url patterns
]
