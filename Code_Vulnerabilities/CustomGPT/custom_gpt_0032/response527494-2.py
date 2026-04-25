
from django.shortcuts import render, redirect
from postman.models import Message

def compose(request):
    if request.method == 'POST':
        recipient = request.POST['recipient']
        subject = request.POST['subject']
        message_body = request.POST['message']

        # Create and save the message
        Message.objects.create(
            sender=request.user,
            recipient=recipient,
            subject=subject,
            body=message_body,
        )
        return redirect('postman:inbox')

    return render(request, 'postman/compose.html')
