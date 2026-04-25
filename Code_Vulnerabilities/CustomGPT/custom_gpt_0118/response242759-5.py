
from allauth.account.views import SignupView
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def get_success_url(self):
        user_type = self.request.POST.get('user_type')

        if user_type == 'architect':
            return '/architect-details/'  # Redirect to business details form
        return super().get_success_url()

# Update urls.py
from django.urls import path
from myapp.views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
]
