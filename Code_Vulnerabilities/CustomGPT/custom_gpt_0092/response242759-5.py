
# forms.py
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect

class CustomSignupForm(SignupForm):
    # Previous code...

    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()

        if user.user_type == 'architect':
            messages.success(request, 'Please complete your business details.')
            return redirect(reverse('business_details'))  # Redirect to a business details form
        return user
