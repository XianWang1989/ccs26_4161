
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("Django is running!")

# In your urls.py
from django.urls import path
from .views import health_check

urlpatterns = [
    path('health/', health_check),
]
