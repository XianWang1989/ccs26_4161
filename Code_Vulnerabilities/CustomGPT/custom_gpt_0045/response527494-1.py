
from django.shortcuts import render
from postman.views import InboxView
from .models import Message  # Assuming you have a Message model

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)  # Replace with your form to handle message sending
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')  # Redirect to inbox or appropriate view
    else:
        form = MessageForm()
    return render(request, 'send_message.html', {'form': form})
