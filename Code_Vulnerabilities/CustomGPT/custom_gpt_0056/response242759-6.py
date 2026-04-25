
# myapp/urls.py

from django.urls import path
from .views import UserTypeView

urlpatterns = [
    path('user-type/', UserTypeView.as_view(), name='user_type'),
    path('business-details/', BusinessDetailsView.as_view(), name='business_details'),
]
