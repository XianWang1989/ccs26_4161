
from django.shortcuts import render
from postman.models import Message

def send_message_view(request):
    if request.method == 'POST':
        # Process the form
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create and send the message
        msg = Message()
        msg.sender = request.user
        msg.recipient = recipient
        msg.subject = subject
        msg.body = message
        msg.save()

        # Redirect or render success message
        return redirect('postman:inbox')

    return render(request, 'send_message.html')
