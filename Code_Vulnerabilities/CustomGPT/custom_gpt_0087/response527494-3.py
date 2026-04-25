
from postman.forms import SendMessageForm

def send_message_view(request):
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect or return a success message
    else:
        form = SendMessageForm()

    return render(request, 'your_template.html', {'form': form})
