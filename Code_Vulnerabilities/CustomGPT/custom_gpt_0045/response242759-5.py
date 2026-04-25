
# myapp/views.py
from django.shortcuts import redirect
from django.contrib.auth import login
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('your_home_view')  # Redirect if already logged in
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = self.signup(form)
        login(self.request, user)
        if user.user_type == 'Architect':
            return redirect('architect_details_view')  # Redirect for special user types
        return redirect('your_home_view')

# Update your urls.py
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
]
