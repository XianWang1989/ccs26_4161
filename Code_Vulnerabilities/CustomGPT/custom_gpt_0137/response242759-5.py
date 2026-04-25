
from django.urls import path
from .views import SignupRedirectView, ArchitectDetailsView

urlpatterns = [
    path('signup/redirect/', SignupRedirectView.as_view(), name='signup_redirect'),
    path('architect-details/', ArchitectDetailsView.as_view(), name='architect_details_signup'),
    # ... other url patterns
]
