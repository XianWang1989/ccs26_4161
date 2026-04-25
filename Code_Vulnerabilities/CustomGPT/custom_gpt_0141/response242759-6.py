
from django.urls import path
from .views import ArchitectDetailsView

urlpatterns = [
    path('architect-details/', ArchitectDetailsView.as_view(), name='architect_details'),
]
