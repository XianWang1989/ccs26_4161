
from allauth.account.views import SignupView
from django.utils.http import is_safe_url
from django.urls import reverse
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def get_success_url(self):
        # Automatically activate user
        self.request.user.is_active = True
        self.request.user.save()
        next_url = self.request.GET.get('next')
        if next_url and is_safe_url(url=next_url, allowed_hosts={self.request.get_host()}):
            return next_url
        return reverse('home')  # Redirect to your desired page

# Add to your urls.py
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
]
