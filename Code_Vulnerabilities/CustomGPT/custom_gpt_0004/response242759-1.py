
from allauth.account.views import SignupView
from django.utils import timezone

class CustomSignupView(SignupView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if self.user:
            self.user.is_active = True
            self.user.save()
        return response
