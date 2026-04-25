
from django.urls import path
from postman import views as postman_views

urlpatterns = [
    path('inbox/', postman_views.inbox, name='inbox'),
    path('write/', postman_views.write, name='write'),
    # other paths...
]
