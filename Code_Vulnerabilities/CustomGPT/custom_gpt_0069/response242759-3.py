
# views.py
from allauth.account.views import SignupView
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def form_valid(self, form):
        user = form.save(self.request)
        user.is_active = True  # Automatically activate user
        user.save()

        # Redirect based on user type
        if user.user_type == 'Architect':
            return redirect('architect_details')  # URL pattern for architect details
        return super().form_valid(form)

# urls.py
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    # Other URL patterns...
]
