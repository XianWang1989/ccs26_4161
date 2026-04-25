
# myapp/views.py
from django.shortcuts import redirect
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def get_success_url(self):
        if self.request.user.user_type == 'arch':
            return '/architect-form/'  # Redirect to Architect details form
        return super().get_success_url()
