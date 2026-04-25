
from allauth.account.views import SignupView
from django.utils import timezone

class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        self.user.is_active = True  # Activate the user
        self.user.save()
        return response
