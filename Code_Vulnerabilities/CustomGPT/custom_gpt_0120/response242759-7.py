
from django.urls import path
from .views import CustomSignupView, BusinessDetailsView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('business-details/', BusinessDetailsView.as_view(), name='business_details'),
]
