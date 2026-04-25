
# myapp/views.py

from django.shortcuts import redirect
from django.urls import reverse
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user_type = request.POST.get('user_type')

        if user_type == 'architect':
            return redirect(reverse('myapp:architect_details'))

        return response
