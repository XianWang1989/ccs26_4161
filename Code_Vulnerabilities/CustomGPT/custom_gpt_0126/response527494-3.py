
# views.py
from postman.forms import SendForm
from django.shortcuts import render, redirect

def send_message(request):
    if request.method == 'POST':
        form = SendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')
    else:
        form = SendForm()
    return render(request, 'postman/send.html', {'form': form})
