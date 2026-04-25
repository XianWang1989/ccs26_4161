
# views.py
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def get_success_url(self):
        user_type = self.request.POST.get('user_type')
        if user_type == 'Architect':
            return reverse('architect_registration')  # URL for additional details
        return super().get_success_url()

# Update your URLs
# urls.py
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('architect-registration/', ArchitectRegistrationView.as_view(), name='architect_registration'),  # Define this view
]
