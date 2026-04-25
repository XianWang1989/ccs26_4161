
from postman.models import Message
from django.shortcuts import redirect, render
from django.contrib import messages

def send_message(request):
    if request.method == 'POST':
        recipients = request.POST['recipients']
        subject = request.POST['subject']
        message = request.POST['message']

        # Create and send the message
        Message.send(request.user, recipients.split(","), subject, message)
        messages.success(request, "Message sent successfully!")
        return redirect('postman:inbox')

    return render(request, 'send_message.html')  # Adjust to your template path
