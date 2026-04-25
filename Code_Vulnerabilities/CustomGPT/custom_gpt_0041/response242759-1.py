
# views.py
from django.urls import reverse
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup

class CustomSignupView(SignupView):
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if self.request.user.is_authenticated:
            self.request.user.is_active = True
            self.request.user.save()
            return complete_signup(request, self.request.user, self.get_success_url(), None)
        return response

# Update urls.py
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
]
