
from allauth.account.views import SignupView
from django.utils import timezone

class CustomSignupView(SignupView):
    def perform_signup(self, request, user):
        user.is_active = True
        user.save()
