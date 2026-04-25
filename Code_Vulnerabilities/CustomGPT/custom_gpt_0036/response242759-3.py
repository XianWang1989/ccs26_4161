
# views.py
from django.shortcuts import render, redirect
from .models import User
from .forms import BusinessDetailsForm  # Create this form for user details

def user_type_redirect(request):
    # Check user type and redirect accordingly
    if request.user.user_type == 'architect':
        return redirect('architect_details_view')  # Name of the architect details page
    elif request.user.user_type == 'client':
        return redirect('client_dashboard')  # Redirect to client dashboard
    return redirect('home')  # Default redirect
