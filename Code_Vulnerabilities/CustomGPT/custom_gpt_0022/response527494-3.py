
from django.shortcuts import render
from postman.views import send

def send_message(request):
    if request.method == 'POST':
        # Handle the message sending logic
        return redirect('postman:inbox')
    return render(request, 'postman/send_message.html')
