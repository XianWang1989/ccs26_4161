
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup
from django.urls import reverse
from django.contrib.auth import login

class CustomSignupView(SignupView):
    def perform_create(self, serializer):
        user = serializer.save(self.request)
        # Automatically activate the user
        user.is_active = True
        user.save()
        # Log the user in and redirect
        login(self.request, user)
        return complete_signup(self.request, user, 
                               'your_success_redirect_url')

