
from django.urls import path
from .views import compose_message

urlpatterns = [
    path('compose/', compose_message, name='compose'),
    # other URL patterns...
]
