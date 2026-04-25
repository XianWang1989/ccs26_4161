
# views.py

from django.shortcuts import redirect
from django.views import View
from django.urls import reverse

class UserTypeRedirectView(View):
    def get(self, request):
        user_type = request.user.user_type
        if user_type == 'Architect':
            return redirect(reverse('architect_details_form'))
        else:
            return redirect(reverse('home'))

# Ensure to set up a URL for this view
