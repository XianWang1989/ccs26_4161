
from django.shortcuts import render, redirect
from postman.views import send

def send_message(request):
    if request.method == 'POST':
        return send(request)
    return render(request, 'send_message.html')
