
from django.shortcuts import render, redirect
from postman.models import Message

def send_message(request):
    if request.method == 'POST':
        recipient = request.POST['recipient']
        subject = request.POST['subject']
        body = request.POST['body']
        Message.objects.create(recipient=recipient, subject=subject, body=body)
        return redirect('postman:inbox')

    return render(request, 'your_template.html')
