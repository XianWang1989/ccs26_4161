
# urls.py
from django.urls import path
from .views import profile_setup, signup_success

urlpatterns = [
    path('profile/setup/', profile_setup, name='profile_setup'),
    path('accounts/signup/success/', signup_success, name='signup_success'),
]
