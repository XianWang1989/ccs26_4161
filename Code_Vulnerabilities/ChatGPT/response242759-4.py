
# views.py

from django.shortcuts import redirect
from django.urls import reverse

def post_signup_view(request):
    user = request.user  # Make sure user is created at this point

    if user.user_type == 'architect':
        return redirect('architect_details')  # Redirect to a new form for architects

    return redirect('home')  # Redirect to main home if no additional info is needed
