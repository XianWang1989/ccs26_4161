
from django.shortcuts import redirect
from postman.models import Message

def send_message(request):
    if request.method == 'POST':
        recipients = request.POST.get('recipients')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # Adjust as necessary to create a Message
        Message.objects.create(subject=subject, message=message, recipients=recipients)
        return redirect('postman:inbox')
    return redirect('postman:compose')
