
# views.py
from django.shortcuts import redirect
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def get_success_url(self):
        if self.request.user.user_type == 'architect':
            return '/architect-details/'  # Replace with your architect details form path
        return super().get_success_url()

# urls.py
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    # Add other urls here
]
