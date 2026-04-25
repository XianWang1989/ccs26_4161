
# views.py
from django.shortcuts import redirect
from allauth.account.views import SignupView
from django.urls import reverse

class CustomSignupView(SignupView):

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            user_type = request.POST.get('user_type')
            if user_type == 'architect':
                # Redirect to extra form for architects
                return redirect('architect_details')  # Define this URL in your urls.py
        return super().dispatch(request, *args, **kwargs)
