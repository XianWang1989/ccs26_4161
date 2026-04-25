
# views.py
from django.shortcuts import render, redirect
from postman import views as postman_views

def send_message(request):
    if request.method == 'POST':
        form = postman_views.MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user  # Set the sender to the logged-in user
            message.save()
            return redirect('postman:inbox')  # Redirect to inbox after sending
    else:
        form = postman_views.MessageForm()

    return render(request, 'postman/send_message.html', {'form': form})
