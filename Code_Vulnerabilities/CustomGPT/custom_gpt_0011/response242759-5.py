
from django.urls import path
from .views import UserTypeSignupView

urlpatterns = [
    path('user-type-signup/', UserTypeSignupView.as_view(), name='user_type_signup'),
]
