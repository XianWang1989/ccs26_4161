
from django.shortcuts import render
from postman.models import Message

def inbox(request):
    messages = Message.objects.filter(recipients=request.user)
    return render(request, 'postman/inbox.html', {'messages': messages})
