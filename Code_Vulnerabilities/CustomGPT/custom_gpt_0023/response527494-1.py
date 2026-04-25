
from django.shortcuts import render, redirect
from postman.forms import MessageForm  # Adjust according to your import paths
from django.contrib.auth.decorators import login_required

@login_required
def send_message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')  # Redirect after sending
    else:
        form = MessageForm()

    return render(request, 'send_message.html', {'form': form})
