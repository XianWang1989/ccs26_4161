
from django.shortcuts import render

def home(request):
    return render(request, 'base.html')  # Ensure 'request' is passed in the context.
