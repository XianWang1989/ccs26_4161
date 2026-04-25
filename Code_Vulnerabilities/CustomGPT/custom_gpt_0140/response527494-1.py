
from django.shortcuts import render, redirect
from postman.models import Message
from postman.forms import MessageForm

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')  # Redirect to the inbox after sending
    else:
        form = MessageForm()

    return render(request, 'send_message.html', {'form': form})
