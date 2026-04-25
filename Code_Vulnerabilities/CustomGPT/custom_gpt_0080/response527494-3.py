
from postman.forms import SendMessageForm
from django.shortcuts import render

def send_message(request):
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')
    else:
        form = SendMessageForm()
    return render(request, 'send_message.html', {'form': form})
