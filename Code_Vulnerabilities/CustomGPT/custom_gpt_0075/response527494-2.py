
from django.shortcuts import render
from postman.models import Message  # Adjust according to your models

def write(request):
    if request.method == 'POST':
        # handle form submission here
        pass
    return render(request, 'postman/write.html', {})
