
from django.urls import path
from .views import update_item

urlpatterns = [
    path('item/update/<int:item_id>/', update_item, name='your_update_view_name'),
]
