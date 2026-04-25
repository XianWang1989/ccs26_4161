
from allauth.account.views import SignupView
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomSignupView(SignupView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if self.request.user.is_authenticated:
            self.request.user.is_active = True
            self.request.user.save()
        return response
