
from django.shortcuts import render, redirect
from postman.forms import PostmanMessageForm

def send_message(request):
    if request.method == 'POST':
        form = PostmanMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')
    else:
        form = PostmanMessageForm()

    return render(request, 'postman/send_message.html', {'form': form})
