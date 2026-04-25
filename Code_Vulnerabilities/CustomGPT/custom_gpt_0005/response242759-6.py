
from django.urls import path
from .views import user_signup_view, architect_details_view

urlpatterns = [
    path('signup/', user_signup_view, name='signup'),
    path('architect-details/', architect_details_view, name='architect_details'),
]
