
from django.urls import path
from .views import custom_signup, BusinessDetailsView

urlpatterns = [
    path('accounts/signup/', custom_signup, name='account_signup'),
    path('business-details/', BusinessDetailsView.as_view(), name='business_details'),
]
