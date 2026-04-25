
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def form_valid(self, form):
        user = form.save(self.request)
        user.is_active = True  # Automatically activate user
        user.save()
        return complete_signup(self.request, user)
