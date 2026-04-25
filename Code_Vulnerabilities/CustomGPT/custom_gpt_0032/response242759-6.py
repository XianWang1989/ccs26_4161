
# urls.py
from django.urls import path
from yourapp.views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('architect-signup-details/', architects_signup_details_view, name='architect_signup_details'),  # Create this view
]
