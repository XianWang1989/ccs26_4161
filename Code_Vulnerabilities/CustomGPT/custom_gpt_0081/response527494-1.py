
from django.urls import path
from postman import views as postman_views

urlpatterns = [
    path('postman/inbox/', postman_views.inbox, name='inbox'),
    path('postman/send/', postman_views.send, name='send'),  # For sending messages
    # Add other required urls here
]
