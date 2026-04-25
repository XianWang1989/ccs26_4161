
from django.shortcuts import render
from postman.forms import MessageForm

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or handle success
    else:
        form = MessageForm()

    return render(request, 'send_message.html', {'form': form})
