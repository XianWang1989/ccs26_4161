
from django.shortcuts import render, redirect
from postman.models import Message  # adjust based on your model

def send_message(request):
    if request.method == 'POST':
        recipient = request.POST['recipient']
        message_content = request.POST['message']

        # Create and send the message (you'll need to adjust the model here)
        Message.objects.create(recipient=recipient, content=message_content)

        return redirect('postman:inbox')  # Redirect to inbox or appropriate page
    return render(request, 'send_message.html')
