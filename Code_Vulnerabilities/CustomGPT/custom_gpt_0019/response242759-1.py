
# views.py
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup
from django.shortcuts import redirect
from django.utils import timezone

class CustomSignupView(SignupView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if response.status_code == 302:  # Redirect after signup
            self.request.user.is_active = True
            self.request.user.date_joined = timezone.now()
            self.request.user.save()
        return response
