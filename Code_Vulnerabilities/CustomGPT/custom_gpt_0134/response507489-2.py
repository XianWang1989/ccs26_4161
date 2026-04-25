
from django.urls import path

urlpatterns = [
    path('form/', FormViewB.as_view(), name='form_view'),
]
