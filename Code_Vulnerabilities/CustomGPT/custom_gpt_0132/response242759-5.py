
# your_app/views.py
from allauth.account.views import SignupView
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def get_success_url(self):
        user_type = self.request.user.user_type
        if user_type == 'architect':
            return '/architect-details/'  # Redirect to additional details page
        return super().get_success_url()
