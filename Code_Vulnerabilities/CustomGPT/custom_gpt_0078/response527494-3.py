
# views.py
from django.shortcuts import render
from postman.forms import SendForm

def send_message(request):
    if request.method == 'POST':
        form = SendForm(request.POST)
        if form.is_valid():
            form.save()  # Send the message
            return redirect('postman:inbox')  # Redirect after sending
    else:
        form = SendForm()

    return render(request, 'send_message.html', {'form': form})
