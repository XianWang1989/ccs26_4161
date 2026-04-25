
from django.shortcuts import render, redirect
from postman.models import Message
from django.contrib import messages

def send_message(request):
    if request.method == 'POST':
        recipient = request.POST['recipient']
        subject = request.POST['subject']
        body = request.POST['body']

        # Create and save the message
        message = Message(recipient=recipient, subject=subject, body=body)
        message.save()  # Adjust according to your model and functionality

        messages.success(request, 'Message sent successfully!')
        return redirect('postman:inbox')  # Redirect to inbox

    return render(request, 'postman/send_message.html')  # Render the form if GET request
