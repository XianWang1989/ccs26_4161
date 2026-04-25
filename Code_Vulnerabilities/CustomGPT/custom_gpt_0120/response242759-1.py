
# views.py
from allauth.account.views import SignupView
from django.contrib.auth import get_user_model

class CustomSignupView(SignupView):
    def perform_signup(self, request, user):
        user.is_active = True  # Automatically activate the user
        user.save()
        super().perform_signup(request, user)
