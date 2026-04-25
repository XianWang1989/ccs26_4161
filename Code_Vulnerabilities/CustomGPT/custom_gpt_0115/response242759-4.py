
from django.shortcuts import redirect

def after_signup(request):
    user = request.user
    if user.user_type == 'Architect':
        return redirect('architect_details')  # Update with your URL
    return redirect('home')  # Fallback URL
