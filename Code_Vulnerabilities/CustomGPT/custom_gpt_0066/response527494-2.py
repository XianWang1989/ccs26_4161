
from django.shortcuts import render, redirect
from postman import views as postman_views

def send_message(request):
    if request.method == 'POST':
        recipients = request.POST.get('recipients')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        # Create the message
        postman_views.send_message(request.user, recipients, subject, body)
        return redirect('postman:inbox')  # Redirect to inbox after sending

    return render(request, 'send.html')
