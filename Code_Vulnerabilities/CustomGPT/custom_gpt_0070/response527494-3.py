
from django.shortcuts import render
from postman.forms import SendMessageForm

def send_message(request):
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the message to database
            # Redirect or render success message
    else:
        form = SendMessageForm()
    return render(request, 'your_template.html', {'form': form})
