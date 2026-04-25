
# views.py
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def perform_signup(self, request, user):
        user.is_active = True
        user.save()
        super().perform_signup(request, user)

        if user.user_type == 'architect':
            return redirect('business_details')  # Your specific URL for business details
