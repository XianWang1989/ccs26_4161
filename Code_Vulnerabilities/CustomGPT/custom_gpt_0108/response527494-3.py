
from django.shortcuts import render, redirect
from postman.models import Message

def send_message_view(request, recipient_username):
    if request.method == 'POST':
        subject = request.POST['subject']
        message_text = request.POST['message']
        recipient = User.objects.get(username=recipient_username)

        message = Message()
        message.sender = request.user
        message.recipient = recipient
        message.subject = subject
        message.message = message_text
        message.save()

        return redirect('postman:inbox')  # Redirect to inbox after sending

    return render(request, 'send_message.html', {'recipient': recipient})
