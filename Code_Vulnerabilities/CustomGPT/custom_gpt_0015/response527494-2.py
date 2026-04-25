
from django.shortcuts import render, redirect
from postman.forms import MessageForm  # Adjust based on your form's location

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the message
            return redirect('postman:inbox')  # Redirect to inbox or another page
    else:
        form = MessageForm()

    return render(request, 'postman/send_message.html', {'form': form})
