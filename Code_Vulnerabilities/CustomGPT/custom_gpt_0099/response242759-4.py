
from allauth.account.views import SignupView
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def get_success_url(self):
        user_type = self.request.POST.get('user_type')
        if user_type == 'arch':
            return '/business-details-form/'
        return super().get_success_url()
