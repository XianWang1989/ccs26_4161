
from allauth.account.utils import complete_signup
from django.urls import reverse

class CustomSignupForm(SignupForm):
    # ... existing code ...

    def save(self, request):
        user = super().save(request)
        if user.user_type == 'architect':
            return reverse('architect_details')
        return super().get_success_url(request, user)
