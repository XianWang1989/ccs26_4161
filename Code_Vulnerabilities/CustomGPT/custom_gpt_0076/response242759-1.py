
from allauth.account.views import SignupView
from django.utils import timezone
from django.contrib.auth.models import User

class CustomSignupView(SignupView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if request.user.is_authenticated:
            user = request.user
            user.is_active = True  # Activate the user
            user.date_joined = timezone.now()  # Timestamp
            user.save()
        return response
