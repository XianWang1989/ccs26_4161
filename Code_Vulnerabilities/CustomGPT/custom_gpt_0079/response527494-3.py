
from django.shortcuts import render
from postman.views import MessageWriteView

def send_message_view(request):
    # Optional: Customize context here if needed
    context = {}
    return render(request, 'postman/send_message.html', context)
