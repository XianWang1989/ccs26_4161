
# views.py
from django.shortcuts import redirect
from allauth.account.views import SignupView

class MySignupView(SignupView):
    def get_success_url(self):
        # Redirect based on user type
        user_type = self.request.POST.get('user_type')
        if user_type == 'architect':
            return '/business-details/'
        return super().get_success_url()
