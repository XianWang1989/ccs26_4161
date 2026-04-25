
from django.shortcuts import render, redirect
from postman.views import send as postman_send

def send_message(request):
    if request.method == "POST":
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Use Django-Postman's send function
        postman_send(request, recipient, subject, message)

        return redirect('postman:inbox')

    return render(request, 'send_message.html')
