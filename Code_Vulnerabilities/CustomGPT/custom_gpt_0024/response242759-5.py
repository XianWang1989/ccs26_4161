
# views.py
from django.shortcuts import redirect, render
from django.urls import reverse

def post_signup_redirect(request):
    user = request.user
    if user.user_type == 'architect':
        return redirect('architect_details')  # Redirect to architect details page
    return redirect('home')
