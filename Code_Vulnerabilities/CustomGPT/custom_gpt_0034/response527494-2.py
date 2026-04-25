
from django.shortcuts import render, redirect
from postman.models import Message
from django.contrib import messages

def send_message(request):
    if request.method == 'POST':
        recipient = request.POST.get('recipients')
        subject = request.POST.get('subject')
        message_body = request.POST.get('message')

        # Create a message instance
        message = Message.objects.create(
            sender=request.user,
            recipients=[recipient],
            subject=subject,
            body=message_body,
        )

        messages.success(request, "Message sent successfully!")
        return redirect('postman:inbox')

    return render(request, 'send_message.html')
