
# urls.py
from django.urls import path
from .views import user_type_redirect

urlpatterns = [
    path('accounts/redirect/', user_type_redirect, name='user_type_redirect'),
]
