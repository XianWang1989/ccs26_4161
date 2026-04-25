
from django.shortcuts import redirect

def redirect_after_signup(request):
    user_type = request.user.user_type
    if user_type == 'architect':
        return redirect('architect_detail_form')  # Replace with the actual name of your URL
    # Default fallback
    return redirect('home')  # General redirect
