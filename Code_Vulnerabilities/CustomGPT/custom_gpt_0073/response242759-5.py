
# myapp/views.py
from django.shortcuts import redirect
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if request.method == 'POST':
            user_type = request.POST.get('user_type')
            if user_type == 'architect':
                return redirect('architect_details')  # URL for additional details form
        return response
