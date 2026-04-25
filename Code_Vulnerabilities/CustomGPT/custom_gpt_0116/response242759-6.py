
# myapp/urls.py
from django.urls import path
from .views import UserTypeRedirectView

urlpatterns = [
    path('redirect/', UserTypeRedirectView.as_view(), name='user_type_redirect'),
]
