
from django.shortcuts import render

def home(request):
    context = {
        'user': request.user,  # This is automatically available through request.user in templates.
    }
    return render(request, 'base.html', context)
