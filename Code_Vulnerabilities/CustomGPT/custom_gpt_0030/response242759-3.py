
# views.py
from django.shortcuts import redirect
from django.urls import reverse
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def form_valid(self, form):
        user = form.save(self.request)
        # Redirect based on user type
        if form.cleaned_data['user_type'] == 'architect':
            return redirect(reverse('architect_details'))  # Redirect to architect details form
        return super().form_valid(form)
