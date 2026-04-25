
# In the view handling signup completion
from django.shortcuts import redirect

def post_signup_view(request):
    user_type = request.POST.get('user_type', None)

    if user_type == 'arch':
        return redirect('business_details_view')  # Redirect to business details form

    return redirect('default_home_view')  # Some default behavior
