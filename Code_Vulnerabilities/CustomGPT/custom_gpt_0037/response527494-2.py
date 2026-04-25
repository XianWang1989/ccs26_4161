
from django.shortcuts import render
from postman.models import Message

def send_message_view(request):
    if request.method == 'POST':
        recipient = request.POST.get('recipient')
        content = request.POST.get('content')
        # Logic to send message using Postman
        Message.objects.create(sender=request.user, recipient=recipient, content=content)
        # Redirect or render a success message
    return render(request, 'post_message.html')
