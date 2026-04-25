
# views.py

from django.shortcuts import render, redirect
from postman.views import send

def send_message(request):
    if request.method == 'POST':
        # Extract data from the form
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Use the Postman send view to send the message
        send(request, recipient, subject, message)
        return redirect('postman:inbox')  # Redirect to inbox after sending

    return render(request, 'send_message.html')
