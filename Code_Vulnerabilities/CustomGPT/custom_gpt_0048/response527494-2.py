
from django.shortcuts import render, redirect
from postman.forms import MessageForm
from django.contrib.auth.decorators import login_required

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Save or process the message
            form.save()
            return redirect('postman:inbox')  # Redirect after sending
    else:
        form = MessageForm()

    return render(request, 'postman/send_message.html', {'form': form})
