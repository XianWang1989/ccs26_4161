
# views.py
from django.shortcuts import redirect
from django.urls import reverse

def signup_complete(request):
    user = request.user
    if user.user_type == 'architect':
        return redirect(reverse('architect_details'))  # Redirect to architect details form
    return redirect('home')  # Default redirect

# urls.py
from django.urls import path
from .views import signup_complete

urlpatterns = [
    # ... other paths ...
    path('signup-complete/', signup_complete, name='signup_complete'),
]
