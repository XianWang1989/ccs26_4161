
# views.py
from allauth.account.views import SignupView
from django.urls import reverse

class CustomSignupView(SignupView):
    def get_success_url(self):
        user_type = self.request.user.user_type
        if user_type == 'architect':
            return reverse('architect_details')  # Define the URL name for the architect form
        return super().get_success_url()
