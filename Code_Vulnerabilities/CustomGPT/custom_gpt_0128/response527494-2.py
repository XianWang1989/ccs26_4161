
from django.shortcuts import render, redirect
from postman.forms import MessageForm  # Ensure you have the correct import

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the message
            return redirect('postman:inbox')  # Redirect to inbox after sending
    else:
        form = MessageForm()

    return render(request, 'postman/send_message.html', {'form': form})
