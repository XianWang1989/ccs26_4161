
from django.urls import path
from .views import redirect_user_after_signup

urlpatterns = [
    path('redirect-after-signup/', redirect_user_after_signup, name='redirect_after_signup'),
]
