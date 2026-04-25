
# forms.py
from django import forms
from allauth.account.forms import SignupForm
from .models import CustomUser  # Assuming you have a CustomUser model

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[('architect', 'Architect'), ('client', 'Client')])

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.is_active = True  # Automatically activate user
        user.save()
        return user
