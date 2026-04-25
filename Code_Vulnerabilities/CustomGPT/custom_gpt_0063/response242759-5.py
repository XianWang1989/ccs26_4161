
from django.urls import path
from yourapp.views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('architect/business-details/', your_business_details_view, name='architect_business_details'),
]
