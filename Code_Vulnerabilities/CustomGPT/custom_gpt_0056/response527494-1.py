
from django.shortcuts import render, redirect
from postman.models import Message
from postman.forms import MessageForm

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user  # Set the sender
            message.save()
            return redirect('postman:inbox')  # Redirect to inbox after sending
    else:
        form = MessageForm()
    return render(request, 'postman/send_message.html', {'form': form})
