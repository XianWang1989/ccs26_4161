
from django.shortcuts import redirect
from django.urls import reverse
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def get_success_url(self):
        if self.request.user.user_type == 'architect':
            return reverse('business_details')
        return super().get_success_url()

# In urls.py
from django.urls import path
from yourapp.views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('business-details/', BusinessDetailsView.as_view(), name='business_details'),
]
