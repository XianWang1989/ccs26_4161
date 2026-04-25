
from django.urls import path
from .views import custom_signup, after_signup

urlpatterns = [
    path('accounts/signup/', custom_signup, name='account_signup'),
    path('accounts/after_signup/', after_signup, name='after_signup'),
    # Add other URLs as needed
]
