
from allauth.account.views import SignupView
from django.urls import reverse

class CustomSignupView(SignupView):
    def get_success_url(self):
        # Redirect based on user type
        user = self.request.user
        if user.user_type == 'architect':
            return reverse('architect_details')  # Replace with your URL
        return super().get_success_url()
