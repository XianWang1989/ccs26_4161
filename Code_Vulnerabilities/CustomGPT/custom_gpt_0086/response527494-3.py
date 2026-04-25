
from django.urls import path
from .views import send_message  # Ensure proper import

urlpatterns = [
    path('send/', send_message, name='send_message'),
    path('postman/', include('postman.urls', namespace='postman')),
    # other urls...
]
