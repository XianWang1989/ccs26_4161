
from postman.models import Message
from django.shortcuts import render
from django.http import HttpResponseRedirect

def send_message(request):
    if request.method == 'POST':
        # Extract sender, recipient, subject, and body from the form
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        # Create and save the message
        message = Message(sender=request.user, recipient=recipient, subject=subject, body=body)
        message.save()
        return HttpResponseRedirect('/postman/inbox/')

    return render(request, 'postman/send_message.html')
