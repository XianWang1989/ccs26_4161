
from django.shortcuts import render
from postman.forms import MessageForm  # Make sure to import the form

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the message
            # Redirect or return a success message
    else:
        form = MessageForm()  # Create a new form instance

    return render(request, 'send_message.html', {'form': form})
