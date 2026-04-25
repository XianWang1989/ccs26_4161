
from django.urls import path
from postman import views

urlpatterns = [
    path('send/', views.send_message, name='send_message'),
]
