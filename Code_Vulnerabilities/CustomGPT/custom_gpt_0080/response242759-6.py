
# urls.py
from django.urls import path
from .views import custom_signup_view

urlpatterns = [
    path('accounts/signup/', custom_signup_view, name='account_signup'),
    path('architect-details/', ArchitectDetailView.as_view(), name='architect_details'),
]
