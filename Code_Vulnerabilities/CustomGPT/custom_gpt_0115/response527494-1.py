
from django.shortcuts import render, redirect
from postman.models import Message
from postman.forms import MessageForm

def send_message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('postman:inbox')
    else:
        form = MessageForm()
    return render(request, 'send_message.html', {'form': form})
