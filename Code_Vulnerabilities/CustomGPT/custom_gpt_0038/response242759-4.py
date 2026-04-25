
# views.py

from allauth.account.views import SignupView
from django.shortcuts import redirect

class CustomSignupView(SignupView):

    def get_success_url(self):
        if self.request.user.user_type == 'architect':
            return '/business-details/'  # your URL for business details form
        return super().get_success_url()
