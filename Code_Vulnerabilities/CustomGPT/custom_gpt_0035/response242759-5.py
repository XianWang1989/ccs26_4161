
from django.shortcuts import redirect
from django.urls import reverse
from allauth.account.views import SignupView

class MySignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        user_type = form.cleaned_data['user_type']

        if user_type == 'arch':
            return redirect(reverse('architect_detail'))  # Redirect to architect detail form
        return response
