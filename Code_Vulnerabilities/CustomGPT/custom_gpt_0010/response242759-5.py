
# views.py
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def check_user_type(request):
    if request.user.user_type == 'architect':
        return redirect('architect_registration')
    return redirect('home')
