
from django.urls import path
from .views import MySignupView

urlpatterns = [
    path('accounts/signup/', MySignupView.as_view(), name='account_signup'),
    # Other URLs...
]
