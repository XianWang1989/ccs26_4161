
# myapp/views.py
from allauth.account.views import SignupView
from django.urls import reverse
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def get_success_url(self):
        user = self.request.user
        if user.user_type == 'arch':
            return reverse('architect_detail_form')  # Redirect to architect form
        return super().get_success_url()
