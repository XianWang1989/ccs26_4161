
from django.shortcuts import render
from postman.models import Message

def inbox_view(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'postman/inbox.html', {'messages': messages})
