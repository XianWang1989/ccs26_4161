
from django.urls import path
from .views import MessageCreateView

urlpatterns = [
    path('send-message/', MessageCreateView.as_view(), name='send_message'),
    # other paths...
]
