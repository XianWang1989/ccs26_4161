
# views.py
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def profile_redirect(request):
    if request.user.user_type == 'architect':
        return redirect('architect_details')  # your URL name for the business details
    return redirect('home')  # or any other default page

# urls.py
from django.urls import path
from .views import profile_redirect

urlpatterns = [
    path('redirect/', profile_redirect, name='profile_redirect'),
]
