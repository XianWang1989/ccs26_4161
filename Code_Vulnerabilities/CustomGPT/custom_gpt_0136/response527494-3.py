
from django.shortcuts import render, redirect
from postman.models import Message

def send_message(request):
    if request.method == 'POST':
        recipient_username = request.POST['recipient']
        subject = request.POST['subject']
        message_body = request.POST['message']

        # Create and save the message
        Message.objects.create(
            sender=request.user,
            recipient=recipient_username,
            subject=subject,
            body=message_body,
        )
        return redirect('postman:inbox')  # Redirect to the inbox

    return render(request, 'send_message.html')
