
from django.urls import path
from .views import log_out_view

urlpatterns = [
    path('logout/', log_out_view, name='logout'),
]
