
from allauth.account.views import SignupView
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def get_success_url(self):
        user = self.request.user
        if user.user_type == 'architect':
            return '/business-details/'  # Redirect to business details page
        return super().get_success_url()

# Update urls.py
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    # Add other URLs
]
