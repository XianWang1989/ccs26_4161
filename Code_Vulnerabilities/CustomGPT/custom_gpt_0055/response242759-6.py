
from django.urls import path
from .views import business_details

urlpatterns = [
    path('business-details/', business_details, name='business_details'),
    # other paths
]
