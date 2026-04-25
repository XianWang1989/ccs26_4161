
# views.py
from allauth.account.views import SignupView
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def get_success_url(self):
        # Redirect based on user type
        user_type = self.request.POST.get('user_type')
        if user_type == 'architect':
            return '/business-details/'  # Profile completion page for Architect
        return super().get_success_url()
