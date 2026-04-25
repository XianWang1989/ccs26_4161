
# urls.py
from django.urls import path
from .views import CustomSendMessageView

urlpatterns = [
    path('send_message/', CustomSendMessageView.as_view(), name='send_message'),
    # Other URLs...
]
