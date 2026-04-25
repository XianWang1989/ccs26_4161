
from django.shortcuts import render
from postman.forms import MessageForm

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the message
            return redirect('postman:inbox')  # Redirect after sending
    else:
        form = MessageForm()  # Create a blank form

    return render(request, 'postman/send_message.html', {'form': form})
