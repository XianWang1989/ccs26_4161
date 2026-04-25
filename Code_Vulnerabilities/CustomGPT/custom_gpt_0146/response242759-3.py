
# views.py
from allauth.account.views import SignupView
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        if form.cleaned_data['user_type'] == 'architect':
            return redirect('architect_business_details')
        return response

# urls.py
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    # other urls...
]
