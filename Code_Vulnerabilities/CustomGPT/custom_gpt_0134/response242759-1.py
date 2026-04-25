
from allauth.account.views import SignupView
from django.utils import timezone

class CustomSignupView(SignupView):
    def complete_signup(self, request, user, *args, **kwargs):
        user.is_active = True  # Activate user
        user.save()
        return super().complete_signup(request, user, *args, **kwargs)
