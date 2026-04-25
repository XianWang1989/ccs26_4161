
from django.urls import path
from .views import custom_signup

urlpatterns = [
    path('accounts/signup/', custom_signup, name='custom_signup'),
    path('architect-details/', ArchitectDetailsView.as_view(), name='architect_details'),
]
