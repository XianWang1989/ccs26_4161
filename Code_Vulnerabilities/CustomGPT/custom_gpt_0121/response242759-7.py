
# yourapp/urls.py

from django.urls import path
from .views import UserSignupView, ArchitectDetailsView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('architect-details/', ArchitectDetailsView.as_view(), name='architect_details'),
]
