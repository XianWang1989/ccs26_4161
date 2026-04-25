
# urls.py
from django.urls import path
from .views import post_signup_redirect

urlpatterns = [
    path('post-signup/', post_signup_redirect, name='post_signup_redirect'),
]
