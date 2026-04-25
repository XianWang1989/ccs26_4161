
from django.shortcuts import render

def home(request):
    return render(request, 'your_app/homepage.html')
