
from django.urls import path
from .views import write_message

urlpatterns = [
    path('write/', write_message, name='write_message'),
]
