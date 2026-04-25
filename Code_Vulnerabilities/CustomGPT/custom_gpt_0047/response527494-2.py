
from django.urls import path
from postman import views as postman_views

urlpatterns = [
    ...,
    path('postman/', postman_views.InboxView.as_view(), name='inbox'),
    path('postman/send/', postman_views.MessageCreationView.as_view(), name='send'),
]
