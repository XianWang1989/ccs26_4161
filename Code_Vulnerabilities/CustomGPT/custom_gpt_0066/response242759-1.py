
# forms.py
from allauth.account.forms import SignupForm
from django import forms
from .models import User

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[('architect', 'Architect'), ('client', 'Client')], required=True)

    def save(self, request):
        user = super().save(request)
        user.is_active = True  # Automatically activate user
        user.save()
        return user
