
# views.py
from django.shortcuts import redirect
from django.urls import reverse
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if request.user.is_authenticated and request.user.user_type == 'architect':
            return redirect(reverse('architect_details_form'))
        return response
