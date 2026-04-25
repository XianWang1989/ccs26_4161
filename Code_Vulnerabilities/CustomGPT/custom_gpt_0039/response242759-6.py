
# urls.py
from django.urls import path
from .views import signup_view, business_details_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('business-details/', business_details_view, name='business_details'),
]
