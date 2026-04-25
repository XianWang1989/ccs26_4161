
from django.shortcuts import render, redirect
from postman.views import send as postman_send

def send_message(request):
    if request.method == 'POST':
        recipient = request.POST['recipient']
        subject = request.POST['subject']
        message = request.POST['message']

        # Call Django-Postman send logic (you may adjust it accordingly)
        postman_send(request, recipient, subject, message)

        return redirect('postman:inbox')  # Redirect to inbox after sending

    return render(request, 'send_message.html')  # Render the template on GET
