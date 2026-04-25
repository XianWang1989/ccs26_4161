
from django.urls import path
from .views import additional_info

urlpatterns = [
    path('additional-info/', additional_info, name='additional_info'),
    # Your other urls
]
