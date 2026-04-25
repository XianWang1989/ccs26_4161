
# urls.py
from django.urls import path
from .views import UserTypeSelectView, ArchitectDetailsView

urlpatterns = [
    path('select_user_type/', UserTypeSelectView.as_view(), name='select_user_type'),
    path('architect_details/', ArchitectDetailsView.as_view(), name='architect_details'),
]
