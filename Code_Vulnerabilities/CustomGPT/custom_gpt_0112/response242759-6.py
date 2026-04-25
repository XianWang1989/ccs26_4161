
from django.urls import path
from .views import ArchitectRegistrationView

urlpatterns = [
    path('architect-registration/', ArchitectRegistrationView.as_view(), name='architect_registration'),
    # Other URLs...
]
