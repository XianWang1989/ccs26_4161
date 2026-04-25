
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTypeRedirectView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.user_type == 'architect':
            return redirect('architect_business_details')  # Redirect to business details form
        else:
            return redirect('home')  # Redirect to home page for other user types
