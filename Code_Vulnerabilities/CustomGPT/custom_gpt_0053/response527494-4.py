
# views.py
from django.shortcuts import render, redirect
from .forms import MessageForm

def write_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('postman:inbox')
    else:
        form = MessageForm()

    return render(request, 'postman/write_message.html', {'form': form})
