
# views.py
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required
def post_signup(request):
    if request.user.user_type == 'architect':
        return redirect('architect_business_details')  # Redirect to the extra form

    return render(request, 'registration/success.html')  # Custom success page
