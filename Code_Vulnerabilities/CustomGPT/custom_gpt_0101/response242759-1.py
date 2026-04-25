
# settings.py

# Automatically activate users after sign up
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True

# Custom signup form to include user type selection
ACCOUNT_SIGNUP_FORM_CLASS = "myapp.forms.CustomSignupForm"

# forms.py
from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[('architect', 'Architect'), ('client', 'Client')])

    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user

# views.py
from django.shortcuts import redirect

def custom_signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            if user.user_type == 'architect':
                return redirect('business_details')
            return redirect('home')
    else:
        form = CustomSignupForm()
    return render(request, 'signup.html', {'form': form})

# urls.py
from django.urls import path
from .views import custom_signup_view

urlpatterns = [
    path('signup/', custom_signup_view, name='custom_signup'),
]
