
# views.py
from allauth.account.views import SignupView
from django.utils import timezone
from django.contrib.auth import get_user_model

class CustomSignupView(SignupView):
    def form_valid(self, form):
        user = super().form_valid(form)
        user.is_active = True  # Activate the user immediately
        user.save()
        return user
