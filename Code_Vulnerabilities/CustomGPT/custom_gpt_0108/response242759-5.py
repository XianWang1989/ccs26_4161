
from django.shortcuts import redirect

def custom_signup_view(request):
    if request.method == 'POST':
        # Handle your signup logic here
        # After signup:
        if user_type == 'architect':
            return redirect('architect_details')  # Redirect to business details page
    else:
        # Render signup form here
        pass
