
# views.py
from django.shortcuts import redirect
from django.urls import reverse
from .forms import CustomSignupForm
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    form_class = CustomSignupForm

    def form_valid(self, form):
        user = form.save(self.request)
        if form.cleaned_data['user_type'] == 'architect':
            return redirect(reverse('architect_details'))
        return super().form_valid(form)
