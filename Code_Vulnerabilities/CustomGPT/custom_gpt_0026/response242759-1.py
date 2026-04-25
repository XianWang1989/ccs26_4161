
# views.py
from allauth.account.views import SignupView
from django.contrib.auth.models import User

class CustomSignupView(SignupView):
    def form_valid(self, form):
        user = super().form_valid(form)
        user.is_active = True
        user.save()
        return user
