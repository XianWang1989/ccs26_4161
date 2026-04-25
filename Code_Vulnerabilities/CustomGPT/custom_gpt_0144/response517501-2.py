from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    return redirect('homepage_url')  # Redirect to homepage after logging out
