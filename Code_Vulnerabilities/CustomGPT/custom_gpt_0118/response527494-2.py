
# views.py
from django.shortcuts import render, redirect
from postman import views as postman_views

def send_message(request):
    if request.method == 'POST':
        # Handle the form submission
        # Validate and send the message using Postman's send function
        form = request.POST
        postman_views.send_message(request, form)
        return redirect('postman:inbox')  # Redirect after sending message
    else:
        return render(request, 'send_message.html')  # Render the form template
