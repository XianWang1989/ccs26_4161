
# views.py
from django.shortcuts import redirect
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def get_success_url(self, request):
        # Check the user type
        user_type = self.form.cleaned_data.get('user_type')
        if user_type == 'architect':
            return '/register-architect/'  # Redirect to architect form
        return super().get_success_url(request)
