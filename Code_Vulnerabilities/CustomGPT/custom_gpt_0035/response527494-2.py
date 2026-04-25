
# views.py
from django.shortcuts import render, redirect
from postman.models import Message  # Adjust import according to your setup

def send_message(request):
    if request.method == "POST":
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        # Create and save your message
        Message.objects.create(
            sender=request.user,
            recipient=recipient,
            subject=subject,
            body=body,
        )
        return redirect('postman:inbox')  # Redirect to inbox after sending

    return render(request, 'send_message.html')
