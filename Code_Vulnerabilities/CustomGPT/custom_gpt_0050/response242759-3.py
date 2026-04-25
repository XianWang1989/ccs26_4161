
# views.py
from allauth.account.views import SignupView
from django.shortcuts import redirect
from django.urls import reverse

class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        user_type = form.cleaned_data.get('user_type')

        if user_type == 'architect':
            return redirect(reverse('architect_registration'))
        return response
