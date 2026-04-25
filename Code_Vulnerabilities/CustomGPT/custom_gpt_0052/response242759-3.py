
# views.py
from django.shortcuts import redirect
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def get_success_url(self):
        user = self.request.user
        if user.user_type == 'architect':
            return '/business-details/'  # Redirect to business details form
        return super().get_success_url()
