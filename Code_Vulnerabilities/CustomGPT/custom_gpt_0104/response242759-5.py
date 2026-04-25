
# views.py
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required
def business_details(request):
    if request.method == 'POST':
        # Process the business details form
        # Save the information associated with the user
        pass
    return render(request, 'business_details.html')
