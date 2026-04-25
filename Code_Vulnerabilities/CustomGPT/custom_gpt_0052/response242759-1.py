
# forms.py
from allauth.account.forms import SignupForm
from django import forms
from .models import UserProfile

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[('architect', 'Architect'), ('client', 'Client')], label='User Type')

    def save(self, request):
        # Call the original save method
        user = super(CustomSignupForm, self).save(request)
        # Automatically activate the user
        user.is_active = True
        user.save()
        return user
