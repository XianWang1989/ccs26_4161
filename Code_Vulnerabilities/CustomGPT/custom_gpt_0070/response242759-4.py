
# views.py
from django.urls import reverse

class CustomSignupView(SignupView):
    # ... previous code ...

    def get_success_url(self):
        user = self.get_user(self.request)
        if user and user.user_type == 'architect':
            return reverse('architect_details')  # Create this URL in your urls.py
        return super().get_success_url()
