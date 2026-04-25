
# views.py
from django.shortcuts import render, redirect
from postman.models import Message
from postman.forms import MessageForm

def send_message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  # save the message
            return redirect('postman:inbox')  # redirect to inbox after sending
    else:
        form = MessageForm()

    return render(request, 'postman/send_message.html', {'form': form})
