
# urls.py
from django.urls import path
from .views import check_user_type

urlpatterns = [
    path('check-user-type/', check_user_type, name='check_user_type'),
]
