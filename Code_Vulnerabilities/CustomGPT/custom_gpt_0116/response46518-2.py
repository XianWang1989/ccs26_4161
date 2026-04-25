
from django.urls import path
from .views import update_item_status

urlpatterns = [
    path('update_status/<int:item_id>/', update_item_status, name='update_status'),
]
