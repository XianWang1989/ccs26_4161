
from django.urls import path
from .views import architect_details

urlpatterns = [
    path('architect-details/', architect_details, name='architect_details'),
]
