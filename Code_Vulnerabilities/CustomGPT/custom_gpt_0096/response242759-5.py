
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if self.request.user.is_authenticated:
            user_type = self.request.POST.get('user_type')
            if user_type == 'arch':
                # Redirect to additional form
                return redirect('additional_form_url')
        return response
