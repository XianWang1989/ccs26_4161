
# views.py
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if request.method == 'POST' and self.get_form().is_valid():
            user_type = self.get_form().cleaned_data.get('user_type')
            if user_type == 'architect':
                return redirect('architect_details')  # URL for architect details
        return response
