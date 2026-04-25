
# views.py
from django.shortcuts import render
from postman.views import MessageWriteView

def send_message_view(request):
    return render(request, 'postman/send_message.html')

# urls.py
from django.urls import path
from .views import send_message_view

urlpatterns = [
    path('send/', send_message_view, name='send_message'),
    path('postman/', include('postman.urls')),
]
