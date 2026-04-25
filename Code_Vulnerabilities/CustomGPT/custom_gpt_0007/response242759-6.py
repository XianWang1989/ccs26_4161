
# In your app's urls.py
from django.urls import path
from .views import custom_signup_view

urlpatterns = [
    path('accounts/signup/', custom_signup_view, name='custom_signup'),
]
