
from django.shortcuts import render
from postman.forms import MessageForm  # Modify according to your actual form

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  # Adjust this according to how you save messages
            return redirect('postman:inbox')  # Redirect after sending
    else:
        form = MessageForm()

    return render(request, 'send_message.html', {'form': form})
