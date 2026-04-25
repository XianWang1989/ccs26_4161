
from django.shortcuts import redirect

class CustomSignupForm(SignupForm):
    # Existing code...

    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()

        if user.user_type == 'architect':
            return redirect('architect_details')  # Redirect to architect details page

        return redirect('home')  # Default redirection for other user types
