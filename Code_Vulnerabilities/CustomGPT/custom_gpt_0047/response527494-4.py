
from django.urls import path
from .views import CustomMessageCreationView

urlpatterns = [
    path('send/', CustomMessageCreationView.as_view(), name='send_message'),
]
