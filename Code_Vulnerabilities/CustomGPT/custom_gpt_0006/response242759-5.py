
# urls.py

from django.urls import path
from .views import custom_signup_view, business_details_view

urlpatterns = [
    path('accounts/signup/', custom_signup_view, name='custom_signup'),
    path('accounts/business-details/', business_details_view, name='business_details'),
]
