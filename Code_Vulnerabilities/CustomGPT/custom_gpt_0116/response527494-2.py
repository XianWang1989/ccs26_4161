
from django.shortcuts import render, redirect
from postman.forms import PostmanForm

def send_message(request):
    if request.method == 'POST':
        form = PostmanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')
    else:
        form = PostmanForm()
    return render(request, 'postman/send_message.html', {'form': form})
