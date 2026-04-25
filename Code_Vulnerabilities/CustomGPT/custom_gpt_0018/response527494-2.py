
from django.shortcuts import render, redirect
from postman.models import Message

def send_message(request):
    if request.method == 'POST':
        recipient = request.POST.get('recipient')
        message_content = request.POST.get('message')
        # Create the message instance
        Message.objects.create(recipient=recipient, content=message_content)
        return redirect('postman:inbox')  # Redirect after sending the message

    return render(request, 'your_template.html')  # Adjust the template name accordingly
