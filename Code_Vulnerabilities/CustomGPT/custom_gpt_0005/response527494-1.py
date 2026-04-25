
from django.shortcuts import render, redirect
from postman.models import Message

def send_message(request):
    if request.method == 'POST':
        recipient = request.POST['recipient']
        subject = request.POST['subject']
        body = request.POST['body']

        # Message creation
        Message.objects.create(sender=request.user, recipient=recipient, subject=subject, body=body)

        return redirect('postman:inbox')  # Redirect to inbox after sending

    return render(request, 'your_template_name.html')  # Adjust as needed
