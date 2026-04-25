
from django.shortcuts import render, redirect
from postman.forms import MessageForm

def send_message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')  # Redirect after a successful send
    else:
        form = MessageForm()

    return render(request, 'your_template_name.html', {'form': form})
