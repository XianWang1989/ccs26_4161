
# yourapp/urls.py
from django.urls import path
from .views import business_details, signup_redirect

urlpatterns = [
    path('business-details/', business_details, name='business_details'),
    path('signup-redirect/', signup_redirect, name='signup_redirect'),
]
