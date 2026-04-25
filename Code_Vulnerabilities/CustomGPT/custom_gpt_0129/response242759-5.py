
# views.py
from django.shortcuts import redirect
from django.urls import reverse
from allauth.account.views import SignupView

class MySignupView(SignupView):
    def get_success_url(self):
        user = self.request.user
        if user.user_type == 'architect':
            return reverse('architect_detail_form')  # Redirect to business details form
        return super().get_success_url()

# urls.py
from django.urls import path
from yourapp.views import MySignupView

urlpatterns = [
    path('accounts/signup/', MySignupView.as_view(), name='account_signup'),
]
