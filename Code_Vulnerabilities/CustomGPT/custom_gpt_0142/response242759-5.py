
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile  # Assuming you have a UserProfile model for business details

@login_required
def business_details(request):
    if request.method == 'POST':
        # Handle form submission for business details here
        ...
        return redirect('home')  # Redirect to a home page or profile page after completing details

    return render(request, 'business_details.html')  # Render your business form
