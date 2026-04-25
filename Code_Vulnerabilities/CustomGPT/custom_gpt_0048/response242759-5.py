
# your_app/views.py
from django.shortcuts import redirect
from django.views import View
from django.urls import reverse

class SignupRedirectView(View):
    def get(self, request):
        user = request.user
        if user.user_type == 'architect':
            return redirect(reverse('architect_registration'))  # Your architect registration form URL
        return redirect(reverse('home'))  # Redirect to a default home page
