
# views.py
from allauth.account.views import SignupView
from django.utils import timezone

class CustomSignupView(SignupView):
    def perform_signup(self, request, user):
        super().perform_signup(request, user)
        # Auto-activate the user
        user.is_active = True
        user.date_joined = timezone.now()
        user.save()
