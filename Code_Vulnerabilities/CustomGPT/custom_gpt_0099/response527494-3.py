
from django.shortcuts import render, redirect
from postman.forms import MessageForm

def write(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')  # Redirect to inbox after sending
    else:
        form = MessageForm()

    return render(request, 'postman/write.html', {'form': form})
