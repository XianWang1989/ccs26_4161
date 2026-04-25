
from django.urls import path
from postman import views as postman_views

urlpatterns = [
    path('postman/inbox/', postman_views.inbox, name='postman:inbox'),
    path('postman/send/', postman_views.send, name='postman:send'),
]
