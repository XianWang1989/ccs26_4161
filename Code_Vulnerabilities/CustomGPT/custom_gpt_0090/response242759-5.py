
# views.py
from django.shortcuts import redirect
from django.views import View

class CustomSignupView(View):
    def post(self, request, *args, **kwargs):
        # Logic to check the user type
        user_type = request.POST.get('user_type')
        if user_type == 'architect':
            return redirect('architect_details')  # Replace with your URL
        return super().post(request, *args, **kwargs)
