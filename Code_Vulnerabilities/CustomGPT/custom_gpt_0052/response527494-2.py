
from django.shortcuts import render, redirect
from postman.models import Message

def send_message_view(request):
    if request.method == 'POST':
        # Handle form submission
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        recipient = request.POST.get('recipient')

        # Create Message instance
        Message.objects.create(
            sender=request.user,
            recipient=recipient,
            subject=subject,
            body=message
        )
        return redirect('postman:inbox')  # Redirect to inbox after sending

    return render(request, 'send_message.html')
