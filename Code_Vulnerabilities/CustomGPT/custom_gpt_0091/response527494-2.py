
from django.shortcuts import render, redirect
from postman.models import PrivateMessage
from django.contrib import messages

def send_message(request):
    if request.method == "POST":
        recipient = request.POST.get('recipient')
        message = request.POST.get('message')

        # Create and send the message
        PrivateMessage.objects.create(
            sender=request.user,
            recipient=recipient,
            subject='New Message',
            body=message
        )

        messages.success(request, 'Message sent successfully!')
        return redirect('postman:inbox')  # Redirect to the inbox after sending

    return render(request, 'send_message.html')
