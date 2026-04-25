
# urls.py
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    # Add the URL for the architect form
    path('architect-form/', ArchitectFormView.as_view(), name='architect_form'),
]
