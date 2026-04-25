
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if self.user:
            self.user.is_active = True
            self.user.save()
            if self.user.user_type == 'architect':
                return redirect('architect_details')  # Your architect detail page
        return response
