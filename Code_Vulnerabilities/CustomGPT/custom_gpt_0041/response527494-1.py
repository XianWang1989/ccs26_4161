
from django.shortcuts import render
from postman.forms import MessageForm

def compose_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')
    else:
        form = MessageForm()

    return render(request, 'postman/compose.html', {'form': form})
