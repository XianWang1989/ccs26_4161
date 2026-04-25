
from django.shortcuts import redirect
from django.urls import reverse

def custom_redirect_view(request):
    user = request.user
    if user.user_type == 'architect':
        return redirect(reverse('architect_details_form'))
    else:
        return redirect('default_page')
