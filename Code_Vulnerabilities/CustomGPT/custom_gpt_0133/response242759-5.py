
# views.py
from django.shortcuts import redirect
from allauth.account.utils import complete_signup

def custom_signup_view(request):
    # Handle signup logic here

    if user.user_type == 'architect':
        return redirect('business_details_url')  # URL of the page for business details
    return complete_signup(request, user)
