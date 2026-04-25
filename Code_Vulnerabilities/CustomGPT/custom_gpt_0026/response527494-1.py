
from django.urls import path
from postman import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('send/', views.send, name='send'),
    # other URL patterns...
]
