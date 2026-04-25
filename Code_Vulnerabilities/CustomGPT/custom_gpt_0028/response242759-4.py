
# views.py
from django.shortcuts import redirect
from django.urls import reverse

def post_signup_view(request):
    if request.user.user_type == 'architect':
        return redirect(reverse('architect_details'))
    return redirect(reverse('home'))

# Inurls.py
from django.urls import path
from .views import CustomSignupView, post_signup_view

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('accounts/post_signup/', post_signup_view, name='post_signup'),
]
