
# your_app/urls.py
from django.urls import path
from .views import SignupRedirectView

urlpatterns = [
    path('accounts/signup/redirect/', SignupRedirectView.as_view(), name='signup_redirect'),
    # other URLs
]
