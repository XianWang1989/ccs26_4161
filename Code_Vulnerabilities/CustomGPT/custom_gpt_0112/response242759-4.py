
from django.shortcuts import redirect
from django.urls import reverse

def post_signup(request, user):
    if user.user_type == 'architect':
        return redirect(reverse('architect_registration'))  # Create the URL pattern for this view
    return redirect(reverse('home'))  # Default redirect
