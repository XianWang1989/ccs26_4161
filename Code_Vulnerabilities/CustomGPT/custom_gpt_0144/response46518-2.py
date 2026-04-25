from django.urls import path
from . import views

urlpatterns = [
    # ... other url patterns ...
    path('update-status/<int:item_id>/', views.update_item_status, name='update_item_status'),
]
