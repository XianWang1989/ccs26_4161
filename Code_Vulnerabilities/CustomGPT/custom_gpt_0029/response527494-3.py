
from django.shortcuts import render, redirect
from postman.forms import MessageForm

def send(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Save the message
            form.save()
            return redirect('postman:inbox')
    else:
        form = MessageForm()
    return render(request, 'postman/send.html', {'form': form})
