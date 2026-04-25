
from django.shortcuts import redirect
from django.contrib import messages

class CustomSignupView(SignupView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if request.user.is_authenticated:
            user = request.user
            user.is_active = True
            user.save()

            if user.user_type == 'architect':
                messages.success(request, 'Please fill in your business details.')
                return redirect('business_details_page')  # Define this URL in your urls.py
        return response
