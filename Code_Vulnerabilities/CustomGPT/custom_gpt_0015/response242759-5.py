
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def redirect_user_after_signup(request):
    if request.user.user_type == 'architect':
        return redirect('architect_details')  # Your view for additional data
    return redirect('default_dashboard')

# Connect this view to the success URL in your signup process
