
from django.shortcuts import render
from postman.forms import MessageForm

def send_message_view(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the message here
            return redirect('postman:inbox')  # Redirect after sending
    else:
        form = MessageForm()
    return render(request, 'postman/send_message.html', {'form': form})
