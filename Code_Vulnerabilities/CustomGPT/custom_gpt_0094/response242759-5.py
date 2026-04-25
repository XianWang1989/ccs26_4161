
# myapp/views.py
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def user_registration_redirect(request):
    if request.user.user_type == 'architect':
        return redirect('architect_details')  # Your URL for the architect details form
    # Continue with other user types or default redirect
    return redirect('home')
