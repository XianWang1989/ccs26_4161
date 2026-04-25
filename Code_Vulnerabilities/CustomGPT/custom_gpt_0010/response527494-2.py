
from postman.views import send_message

def custom_send_message(request):
    if request.method == 'POST':
        # Process form submission
        form = YourMessageForm(request.POST)
        if form.is_valid():
            form.save()  # or handle sending message logic
            return redirect('postman:inbox')
    else:
        form = YourMessageForm()
    return render(request, 'your_template.html', {'form': form})
