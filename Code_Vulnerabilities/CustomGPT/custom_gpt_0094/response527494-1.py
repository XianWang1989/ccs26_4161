
from django.urls import path
from postman import views

urlpatterns = [
    path('inbox/', views.inbox_view, name='inbox'),
    path('send/', views.send_view, name='send_message'),
]
