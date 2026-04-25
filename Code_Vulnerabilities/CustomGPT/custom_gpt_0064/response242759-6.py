
# urls.py
from django.urls import path
from .views import MySignupView

urlpatterns = [
    path('accounts/signup/', MySignupView.as_view(), name='account_signup'),
    path('business-details/', BusinessDetailsView.as_view(), name='business_details'),
]
