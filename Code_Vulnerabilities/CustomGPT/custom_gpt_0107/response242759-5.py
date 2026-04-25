
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def profile_setup(request):
    if request.method == 'POST':
        # Handle the form submission for business details
        # (save data to user)
        return redirect('home')  # or another page

    return render(request, 'profile_setup.html')

def signup_success(request):
    user_type = request.user.user_type
    if user_type == 'architect':
        return redirect('profile_setup')  # Redirect to setup page

    return redirect('home')  # Default redirect
