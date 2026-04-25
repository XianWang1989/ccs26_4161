
from django.shortcuts import render
from postman.forms import MessageForm

def send_message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect after a successful message send
            return redirect('postman:inbox')
    else:
        form = MessageForm()

    return render(request, 'your_template/send_message.html', {'form': form})
