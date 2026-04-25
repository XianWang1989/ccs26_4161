
from django.urls import path
from .views import CustomSignupView, custom_redirect_view

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('accounts/redirect/', custom_redirect_view, name='custom_redirect'),
]
