
# views.py
from django.shortcuts import redirect
from django.contrib.auth import login
from django.views import View
from django.urls import reverse

class CustomSignupView(View):
    def post(self, request, *args, **kwargs):
        user = self.get_user_from_signup_form(request)
        if user:
            login(request, user)
            if user.userprofile.user_type == 'Architect':
                return redirect(reverse('architect_business_details'))  # URL for architect details
            # Handle other user types similarly
        return redirect('default')

    def get_user_from_signup_form(self, request):
        # Include logic to get user from signup process
        pass
