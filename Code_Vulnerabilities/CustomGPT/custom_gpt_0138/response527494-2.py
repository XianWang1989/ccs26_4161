
from django.shortcuts import render
from postman import views as postman_views

def send_message_view(request):
    return postman_views.send_message(request)
