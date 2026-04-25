
from django.urls import path
from .views import CustomSendView

urlpatterns = [
    path('send/', CustomSendView.as_view(), name='send'),
    # other URL patterns...
]
