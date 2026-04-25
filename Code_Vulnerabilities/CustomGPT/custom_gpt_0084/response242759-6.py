
# urls.py
from django.urls import path
from .views import custom_signup, signup_complete

urlpatterns = [
    path('accounts/signup/', custom_signup, name='custom_signup'),
    path('signup-complete/', signup_complete, name='signup_complete'),
]
