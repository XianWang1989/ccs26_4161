
from django.shortcuts import render, redirect
from postman.forms import ComposeForm

def compose(request):
    if request.method == 'POST':
        form = ComposeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('postman:inbox')
    else:
        form = ComposeForm()
    return render(request, 'postman/compose.html', {'form': form})
