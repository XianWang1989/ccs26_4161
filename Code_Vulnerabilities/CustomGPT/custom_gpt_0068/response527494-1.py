
from django.shortcuts import render, redirect
from postman.views import CreateMessage
from postman.models import Message

def send_message(request):
    if request.method == 'POST':
        form = CreateMessage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')  # Redirect to inbox after sending
    else:
        form = CreateMessage()
    return render(request, 'your_app/send_message.html', {'form': form})
