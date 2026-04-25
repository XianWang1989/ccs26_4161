
# views.py
from postman.views import SendMessage
from django.shortcuts import render

def send_message_view(request):
    if request.method == 'POST':
        # Handle posted form data if needed
        # Typically the SendMessage view would manage this
        return SendMessage.as_view()(request)

    return render(request, 'postman/send_message.html')
