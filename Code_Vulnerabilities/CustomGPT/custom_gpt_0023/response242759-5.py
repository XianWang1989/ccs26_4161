
# views.py
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def create(self, request):
        user = super().create(request)
        user.is_active = True
        user.save()

        # Redirect based on user type
        if user.user_type == 'architect':
            return redirect('architect_details')  # Update this with your actual URL name

        return user
