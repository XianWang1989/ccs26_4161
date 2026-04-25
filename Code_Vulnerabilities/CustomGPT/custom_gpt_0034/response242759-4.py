
from django.urls import path
from yourapp.views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('architect-details/', ArchitectDetailsView.as_view(), name='architect_details'),  # View for business details
]
