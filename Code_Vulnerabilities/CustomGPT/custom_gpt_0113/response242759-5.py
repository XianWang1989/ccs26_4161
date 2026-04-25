
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def post_signup_redirect(request):
    user = request.user
    if user.user_type == 'arch':
        return redirect(reverse('architect_details_form'))
    else:
        return redirect(reverse('home'))
