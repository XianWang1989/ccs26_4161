
# views.py
from django.shortcuts import redirect
from django.urls import reverse

def architect_details_view(request):
    if request.method == 'POST':
        # Process the business details form
        pass  # Add your form processing logic here
    return render(request, 'architect_details.html')
