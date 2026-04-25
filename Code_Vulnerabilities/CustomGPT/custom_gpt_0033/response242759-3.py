
# views.py
from django.shortcuts import redirect
from allauth.account.views import SignupView

class CustomSignupView(SignupView):

    def get_success_url(self):
        user_type = self.request.user.user_type
        if user_type == 'Architect':
            return '/architect-details/'  # Redirect to architect details form
        return super().get_success_url()

# urls.py
from yourapp.views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
]
