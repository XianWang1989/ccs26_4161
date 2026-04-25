
from django.shortcuts import redirect
from django.urls import reverse
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        user_type = form.cleaned_data.get('user_type')

        if user_type == 'arch':
            return redirect(reverse('architect_details'))  # Redirect to architect details page

        return response
