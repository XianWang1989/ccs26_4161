
from django.shortcuts import redirect, render
from django.urls import reverse
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def get_success_url(self):
        user_type = self.request.user.user_type
        if user_type == 'architect':
            return reverse('architect_detail')
        return super().get_success_url()

# Add to your urls.py
from django.urls import path

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
]
