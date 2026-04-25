
# views.py
from django.shortcuts import redirect
from django.urls import reverse

def post_signup_redirect(request):
    user_type = request.user.user_type
    if user_type == 'architect':
        return redirect(reverse('architect_details'))
    return redirect(reverse('home'))
