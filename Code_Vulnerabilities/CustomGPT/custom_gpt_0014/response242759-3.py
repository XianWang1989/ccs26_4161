
# views.py
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth import get_user_model

class CustomSignupView(View):
    def post(self, request):
        form = CustomSignupForm(request.POST)

        if form.is_valid():
            user = form.save(request)
            user_type = form.cleaned_data['user_type']

            if user_type == 'architect':
                return redirect('architect_details')
            else:
                return redirect('client_dashboard')

        return self.form_invalid(form)

# Update URLs
# urls.py
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    # Additional paths...
]
