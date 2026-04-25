
from django.shortcuts import render, redirect
from postman.models import Message

def send_message(request):
    if request.method == 'POST':
        recipient = request.POST['recipient']
        subject = request.POST['subject']
        body = request.POST['body']

        # Create and send the message
        message = Message(sender=request.user, recipient=recipient, subject=subject, body=body)
        message.save()

        return redirect('postman:inbox')  # Redirect to the inbox after sending

    return render(request, 'send_message.html')  # Render the template if GET request
