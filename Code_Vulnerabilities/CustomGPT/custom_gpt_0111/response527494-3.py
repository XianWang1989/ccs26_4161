
from postman.forms import MessageForm
from django.shortcuts import render, redirect

def send_message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')  # Redirect after success
    else:
        form = MessageForm()
    return render(request, 'postman/send_message.html', {'form': form})
