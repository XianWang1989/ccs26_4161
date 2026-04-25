
from django.shortcuts import render, redirect
from postman.models import Message  # Adjust according to your models

def send(request):
    if request.method == 'POST':
        recipient = request.POST['recipient']
        subject = request.POST['subject']
        message = request.POST['message']

        # Create and save the message instance
        Message.objects.create(
            sender=request.user,
            recipient=recipient,
            subject=subject,
            body=message
        )

        # Redirect to inbox or any other page after sending
        return redirect('postman:inbox')

    return render(request, 'postman/send_message.html')  # Render the form if GET request
