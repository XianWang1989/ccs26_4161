
from django.shortcuts import render, redirect
from postman.models import Message

def send_message(request):
    if request.method == 'POST':
        recipient = request.POST['recipient']
        subject = request.POST['subject']
        message = request.POST['message']
        # Create and save the message
        Message.objects.create(
            sender=request.user,
            recipient=recipient,
            subject=subject,
            message=message,
        )
        return redirect('postman:inbox')  # Redirect to inbox after sending
    return render(request, 'send_message.html')  # Render form
