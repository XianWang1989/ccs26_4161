
# views.py
from django.shortcuts import render

@login_required
def architect_details(request):
    if request.method == 'POST':
        # Handle the architect business details form submission
        pass

    return render(request, 'architect_details.html')
