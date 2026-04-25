
from django.urls import path
from postman.views import inbox, write

urlpatterns = [
    path('inbox/', inbox, name='inbox'),
    path('write/', write, name='write'),
]
