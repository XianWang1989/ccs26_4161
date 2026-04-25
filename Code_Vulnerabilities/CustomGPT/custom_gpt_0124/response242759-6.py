
# urls.py
from django.urls import path
from .views import ArchitectDetailsView, signup_view

urlpatterns = [
    path('signup/', signup_view, name='account_signup'),
    path('architect/details/', ArchitectDetailsView.as_view(), name='architect_details'),
]
