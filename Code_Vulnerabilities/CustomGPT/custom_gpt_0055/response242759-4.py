
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def business_details(request):
    if request.method == 'POST':
        # Handle form submission for business details
        pass
    return render(request, 'business_details.html')
