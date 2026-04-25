
# views.py

from django.shortcuts import render
from postman.forms import MessageForm

def send_message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Here you would save the message or process it
            form.save()  # Ensure your form is configured to handle this
            return redirect('postman:inbox')  # Redirect after post
    else:
        form = MessageForm()

    return render(request, 'send_message.html', {'form': form})
