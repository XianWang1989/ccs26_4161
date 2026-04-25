
from django.shortcuts import redirect
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def form_valid(self, form):
        user = form.save(self.request)
        if form.cleaned_data['user_type'] == 'architect':
            return redirect('architect_details')  # Redirect to architect details form
        return super().form_valid(form)
