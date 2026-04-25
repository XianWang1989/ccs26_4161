
from postman.views import send, inbox
from django.shortcuts import render

def custom_send_view(request):
    if request.method == 'POST':
        # Process the form as needed
        return send(request)
    return render(request, 'your_template/send_message.html')
