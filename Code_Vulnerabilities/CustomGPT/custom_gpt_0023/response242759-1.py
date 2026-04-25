
# views.py
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup

class CustomSignupView(SignupView):
    def create(self, request):
        user = super().create(request)
        user.is_active = True
        user.save()
        return user
