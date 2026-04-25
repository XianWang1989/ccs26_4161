
# urls.py
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('architect-registration/', ArchitectRegistrationView.as_view(), name='architect_registration'),
    # ... other URL patterns ...
]
