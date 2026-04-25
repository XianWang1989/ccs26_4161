
# yourapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def architect_details(request):
    if request.method == 'POST':
        # Process the form with business details
        # Save the details...
        return redirect('home')  # Redirect to home or another page
    return render(request, 'architect_details.html')

# In the original signup view
def signup_complete(request):
    user_type = request.user.user_type  # Get user type from user model
    if user_type == 'architect':
        return redirect('architect_details')
    return redirect('home')

# Update your urls.py
from django.urls import path
from .views import architect_details, signup_complete

urlpatterns = [
    path('architect/details/', architect_details, name='architect_details'),
    path('signup/complete/', signup_complete, name='signup_complete'),
]
