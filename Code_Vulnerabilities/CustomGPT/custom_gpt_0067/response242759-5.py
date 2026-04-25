
from django.shortcuts import redirect
from django.urls import reverse

class CustomSignupForm(SignupForm):
    # ... (previous code)

    def save(self, request):
        user = super().save(request)
        if user.user_type == 'architect':
            return redirect(reverse('architect_details'))  # Replace with your URL
        return redirect('/')
