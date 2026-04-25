
# myapp/urls.py
from django.urls import path
from .views import user_registration_redirect

urlpatterns = [
    path('redirect/', user_registration_redirect, name='user_registration_redirect'),
]
