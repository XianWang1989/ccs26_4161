
# myapp/views.py
from django.shortcuts import redirect
from django.views import View

class UserTypeRedirectView(View):
    def post(self, request, *args, **kwargs):
        user_type = request.POST.get('user_type')
        if user_type == 'architect':
            return redirect('architect_details')  # URL where the architect form is located
        return redirect('home')  # Redirect to home for other user types
