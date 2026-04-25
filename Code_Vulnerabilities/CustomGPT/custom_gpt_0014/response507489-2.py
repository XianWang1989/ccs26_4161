
from django.urls import path
from .views import FormViewB

urlpatterns = [
    path('my-form/', FormViewB.as_view(), name='my_form'),
]
