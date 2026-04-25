
# urls.py
from django.urls import path
from .views import architect_details, signup_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('architect/details/', architect_details, name='architect_details'),
]
