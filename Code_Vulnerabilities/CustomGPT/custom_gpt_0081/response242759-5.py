
from django.urls import path
from .views import UserTypeRedirectView

urlpatterns = [
    # Other URLs...
    path('account/signup/success/', UserTypeRedirectView.as_view(), name='signup_success'),
]
