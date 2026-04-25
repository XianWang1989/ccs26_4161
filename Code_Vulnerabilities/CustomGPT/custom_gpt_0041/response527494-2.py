
from django.urls import path
from .views import compose_message

urlpatterns = [
    path('send/', compose_message, name='compose_message'),
]
