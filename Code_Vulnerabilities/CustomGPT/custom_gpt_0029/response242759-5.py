
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def get_success_url(self):
        if self.user.user_type == 'architect':
            return '/additional-architect-details/'
        return super().get_success_url()
