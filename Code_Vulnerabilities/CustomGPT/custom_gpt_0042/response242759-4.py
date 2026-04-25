
# views.py (continued)
from django.shortcuts import redirect
from django.urls import reverse

class CustomSignupView(SignupView):
    def form_valid(self, form):
        user = super().form_valid(form)
        user.is_active = True
        user.save()

        # Redirect based on user type
        if user.user_type == 'architect':
            return redirect('architect_business_details')
        return super().form_valid(form)
