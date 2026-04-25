# views.py
from django.shortcuts import redirect

def login_redirect_view(request):
    redirect_url = request.session.pop('post_signup_redirect', '/default/')
    return redirect(redirect_url)
