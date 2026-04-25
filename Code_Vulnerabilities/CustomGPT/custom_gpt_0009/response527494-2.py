
from django.shortcuts import render, redirect
from postman.forms import MessageForm  # Assuming you have a form defined for messages

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the message to the database
            return redirect('postman:inbox')  # Redirect to the inbox after sending
    else:
        form = MessageForm()

    return render(request, 'postman/send_message.html', {'form': form})
