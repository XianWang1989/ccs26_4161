
from django.urls import path
from .views import RedirectAfterSignupView

urlpatterns = [
    path('accounts/signup/', your_signup_view, name='account_signup'),
    path('accounts/redirect/', RedirectAfterSignupView.as_view(), name='redirect_after_signup'),
    # Other paths...
]
