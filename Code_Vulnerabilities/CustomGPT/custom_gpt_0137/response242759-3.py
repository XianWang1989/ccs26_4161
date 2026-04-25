
# views.py
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View

class SignupRedirectView(View):
    def get(self, request):
        user_type = request.GET.get('user_type', None)

        if user_type == 'architect':
            return redirect(reverse('architect_details_signup'))  # Redirect to architect details form

        return redirect(reverse('home'))  # Default redirect after signup
