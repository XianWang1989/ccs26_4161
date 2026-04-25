
from django.urls import path
from yourapp.views import UserTypeRedirectView

urlpatterns = [
    path('accounts/signup/', UserTypeRedirectView.as_view(), name='account_signup'),
    # Add further URL configurations
]
