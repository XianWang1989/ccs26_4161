
# views.py
from django.shortcuts import redirect
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def form_valid(self, form):
        user = form.save(self.request)
        # Redirect based on user type
        if user.user_type == 'Architect':
            return redirect('architect_details')
        return super().form_valid(form)
