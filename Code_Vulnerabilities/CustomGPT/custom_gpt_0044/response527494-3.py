
from postman.forms import MessageForm
from django.shortcuts import render, redirect
from django.contrib import messages

def send_message_view(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully!")
            return redirect('postman:inbox')
    else:
        form = MessageForm()
    return render(request, 'send_message.html', {'form': form})
