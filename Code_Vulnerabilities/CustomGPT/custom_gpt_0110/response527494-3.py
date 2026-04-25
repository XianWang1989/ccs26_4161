
from django.shortcuts import render
from postman.forms import MessageForm  # Adjust according to your imports

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')  # Redirect after a successful send
    else:
        form = MessageForm()
    return render(request, 'send_message.html', {'form': form})
