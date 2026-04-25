
# urls.py
from django.urls import path
from .views import ArchitectBusinessDetailsView  # assume you create this view

urlpatterns = [
    path('business-details/', ArchitectBusinessDetailsView.as_view(), name='architect_business_details'),
]
