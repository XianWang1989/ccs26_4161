
# views.py
from django.shortcuts import render, redirect
from postman.forms import SendMessageForm

def send_message_view(request):
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')  # Redirect to inbox after sending
    else:
        form = SendMessageForm()

    return render(request, 'send_message.html', {'form': form})
