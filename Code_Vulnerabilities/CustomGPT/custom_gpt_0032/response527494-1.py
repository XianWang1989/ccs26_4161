
from django.urls import path
from postman import views as postman_views

urlpatterns = [
    path('inbox/', postman_views.inbox, name='inbox'),
    path('sent/', postman_views.sent, name='sent'),
    path('compose/', postman_views.compose, name='compose'),
    # other URLs here...
]
