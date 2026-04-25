
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def form_valid(self, form):
        user = super().form_valid(form)
        user.is_active = True
        user.save()

        if user.user_type == 'architect':
            return redirect('business_details')  # URL name for the business details page

        return redirect('home')  # Fallback URL

# In urls.py, make sure you have the URL for business details defined
