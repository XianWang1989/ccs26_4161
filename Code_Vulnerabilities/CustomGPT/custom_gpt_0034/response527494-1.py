
from django.urls import path
from postman import views as postman_views

urlpatterns = [
    path('send/', postman_views.send, name='send_message'),
    path('inbox/', postman_views.inbox, name='inbox'),
    # other urls...
]
