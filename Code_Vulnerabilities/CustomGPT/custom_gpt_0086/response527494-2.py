
from django.shortcuts import render
from postman.models import MessageForm  # Adjust as necessary

def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            # You can redirect or display a success message
    else:
        form = MessageForm()

    return render(request, 'message_form.html', {'form': form})
