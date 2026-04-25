
from django.urls import path
from .views import architect_details_view, CustomSignupView

urlpatterns = [
    path('architect-details/', architect_details_view, name='architect_details'),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
]
