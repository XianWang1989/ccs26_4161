
from django.shortcuts import render, redirect
from postman.forms import MessageForm  # Make sure this refers to your MessageForm

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  # Adjust saving logic as per your model
            return redirect('postman:inbox')  # Redirect to inbox or a success page
    else:
        form = MessageForm()

    return render(request, 'send_message.html', {'form': form})
