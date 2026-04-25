
# views.py
from django.shortcuts import render

def architect_details_view(request):
    if request.method == 'POST':
        # Process the form data here
        pass
    return render(request, 'architect_details.html')  # Create this template
