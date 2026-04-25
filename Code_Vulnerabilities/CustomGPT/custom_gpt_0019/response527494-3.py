
from django.shortcuts import render
from postman.views import SendMessageView

def my_send_message_view(request):
    return SendMessageView.as_view()(request)
