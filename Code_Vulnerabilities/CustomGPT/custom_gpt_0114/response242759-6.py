
from django.urls import path
from .views import CustomSignupView    

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('architect-details/', ArchitectDetailView.as_view(), name='architect_details'),
]
