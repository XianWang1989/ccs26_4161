
from django.urls import path
from postman import views as postman_views

urlpatterns = [
    path('postman/send/', postman_views.send_message, name='postman:send'),
    path('postman/inbox/', postman_views.inbox, name='postman:inbox'),
    # other URLs
]
