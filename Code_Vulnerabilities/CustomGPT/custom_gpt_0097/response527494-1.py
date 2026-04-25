
from django.shortcuts import render, redirect
from postman.views import send

def send_message(request):
    if request.method == 'POST':
        form = send(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')
    else:
        form = send()
    return render(request, 'send_message.html', {'form': form})
