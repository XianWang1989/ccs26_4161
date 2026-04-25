
# forms.py
from django import forms
from allauth.account.forms import SignupForm
from .models import User

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[('architect', 'Architect'), ('client', 'Client')])

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']  # Assuming you have a user_type field
        user.save()
        return user
