
from django.shortcuts import redirect
from django.contrib.auth import logout

def log_out_view(request):
    logout(request)
    return redirect('/')
