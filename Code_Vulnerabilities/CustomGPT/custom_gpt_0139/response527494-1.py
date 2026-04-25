
from django.urls import path
from postman import views as postman_views

urlpatterns = [
    path('postman/inbox/', postman_views.inbox, name='inbox'),
    path('postman/send/<int:user_id>/', postman_views.send, name='send'),
    # Add your other URL patterns here
]
