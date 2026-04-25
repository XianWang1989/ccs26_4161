
# urls.py
from django.urls import path
from .views import CustomSignupView, business_details

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('business-details/', business_details, name='business_details'),
]
