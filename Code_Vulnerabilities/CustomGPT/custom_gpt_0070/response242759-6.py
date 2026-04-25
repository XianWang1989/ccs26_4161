
# urls.py
from django.urls import path
from .views import CustomSignupView, architect_details_view

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_sign_up'),
    path('architect/details/', architect_details_view, name='architect_details'),
]
