
# views.py
from django.shortcuts import redirect
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def get_success_url(self):
        user_type = self.request.POST.get('user_type')
        if user_type == 'architect':
            return '/architect-details/'  # Redirect to architect details page
        return super().get_success_url()
