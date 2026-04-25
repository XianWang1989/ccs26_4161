
# views.py
from django.shortcuts import redirect
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        user_type = form.cleaned_data.get('user_type')

        if user_type == 'Architect':
            return redirect('business_details')  # Redirect to business details page

        return response

# urls.py
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('business-details/', YourBusinessDetailsView.as_view(), name='business_details'),
]
