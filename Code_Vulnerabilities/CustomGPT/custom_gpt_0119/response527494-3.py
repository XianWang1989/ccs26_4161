
from django.shortcuts import render
from postman.models import Message

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')  # Redirect to inbox or wherever needed
    else:
        form = MessageForm()
    return render(request, 'postman/send_message.html', {'form': form})
