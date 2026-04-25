
from django.shortcuts import render, redirect
from postman.views import send_message

def send_message_view(request):
    if request.method == 'POST':
        # Handle form submission
        return send_message(request)
    return render(request, 'your_template.html')
