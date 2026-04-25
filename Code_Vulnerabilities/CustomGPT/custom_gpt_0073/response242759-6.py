
# urls.py
from django.urls import path
from myapp.views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('architect-details/', ArchitectDetailsView.as_view(), name='architect_details'),  # Additional form view
]
