
# views.py
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def post_signup_redirect(request):
    if request.user.user_type == 'architect':
        return redirect('architect_details')
    return redirect('home')

# urls.py
from yourapp.views import post_signup_redirect

urlpatterns = [
    path('accounts/signup/', post_signup_redirect, name='post_signup_redirect'),
]
