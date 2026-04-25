
# myapp/urls.py
from django.urls import path
from .views import CustomSignupView, ArchitectDetailsView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='custom_signup'),
    path('additional-form/', ArchitectDetailsView.as_view(), name='architect_details'),
]
