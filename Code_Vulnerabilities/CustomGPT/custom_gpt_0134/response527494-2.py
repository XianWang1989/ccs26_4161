
from django.shortcuts import render, redirect
from postman.forms import MessageForm

def send_message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the message
            return redirect('postman:inbox')  # Redirect to Inbox after sending
    else:
        form = MessageForm()  # Create a new empty form

    return render(request, 'postman/send_message.html', {'form': form})
