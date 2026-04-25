
from django.urls import path
from postman import views as postman_views

urlpatterns = [
    path('inbox/', postman_views.inbox, name='inbox'),
    path('message/<int:message_id>/', postman_views.message, name='message'),
    # other paths...
]
