
from django.shortcuts import render, redirect
from postman.forms import MessageForm

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')  # Redirect to inbox after sending
    else:
        form = MessageForm()  # Initialize a blank form
    return render(request, 'send_message.html', {'form': form})
