
# views.py
from django.shortcuts import render
from postman.forms import MessageForm  # Replace with the correct import, if necessary

def send_message_view(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            # Save the message
            form.save()  # Adjust according to how you need to save it
            return redirect('postman:inbox')  # Redirect after posting
    else:
        form = MessageForm()

    return render(request, 'your_template.html', {'form': form})
