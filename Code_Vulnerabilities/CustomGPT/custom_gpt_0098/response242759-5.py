
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View

class RedirectAfterSignupView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.user_type == 'architect':
            return redirect(reverse('architect-registration'))  # Your architect form page

        return redirect('home')  # Redirect to home or dashboard
