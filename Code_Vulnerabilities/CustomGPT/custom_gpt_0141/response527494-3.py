
from django.shortcuts import render
from postman.models import Message
from postman.forms import MessageForm

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or render success message
    else:
        form = MessageForm()

    return render(request, 'postman/send_message.html', {'form': form})
