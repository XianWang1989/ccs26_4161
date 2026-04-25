
# views.py
from allauth.account.views import SignupView
from django.urls import reverse
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def form_valid(self, form):
        user = form.save(self.request)
        user_type = form.cleaned_data.get('user_type')
        if user_type == 'architect':
            return redirect('architect_details')  # Redirect to architect details page
        return super().form_valid(form)

# Integrate the view in urls.py
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
]
