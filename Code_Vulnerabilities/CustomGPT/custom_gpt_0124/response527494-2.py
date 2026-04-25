
from django.shortcuts import render, redirect
from postman.forms import MessageForm  # Assuming you have a form defined
from postman.models import Message

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user  # Assign the sender to the current user
            message.save()
            return redirect('postman:inbox')
    else:
        form = MessageForm()
    return render(request, 'send_message.html', {'form': form})
