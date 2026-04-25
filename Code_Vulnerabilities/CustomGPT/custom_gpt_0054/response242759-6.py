
# urls.py
from django.urls import path
from .views import post_signup

urlpatterns = [
    path('post-signup/', post_signup, name='post_signup'),
]
