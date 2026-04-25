
# views.py
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup
from django.contrib.auth import login

class CustomSignupView(SignupView):
    def signup(self, request, **kwargs):
        user = super().signup(request, **kwargs)
        user.is_active = True  # Activate user
        user.save()
        login(request, user)
        return complete_signup(request, user, self.get_success_url())
