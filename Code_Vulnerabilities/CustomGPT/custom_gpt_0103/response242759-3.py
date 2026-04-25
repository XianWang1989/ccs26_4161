
from django.shortcuts import redirect
from django.urls import reverse
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        user_type = form.cleaned_data.get('user_type')

        if user_type == 'Architect':
            return redirect(reverse('architect_details'))  # Redirect to additional details page

        return response

# In your urls.py
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('architect/details/', ArchitectDetailsView.as_view(), name='architect_details'),
]
