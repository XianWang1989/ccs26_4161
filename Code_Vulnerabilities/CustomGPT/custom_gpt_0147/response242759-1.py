
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup
from django.urls import reverse
from django.utils import timezone

class CustomSignupView(SignupView):
    def perform_signup(self, request, user):
        user.is_active = True  # Activate the user
        user.save()
        complete_signup(request, user, 'your_redirect_url']

# In your urls.py
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
]
